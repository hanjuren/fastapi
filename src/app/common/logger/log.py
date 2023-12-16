import logging
import os
import sys

from loguru import logger

from app.common.conf.path_conf import LogPath
from app.common.conf.service_conf import settings


class InterceptHandler(logging.Handler):
    loglevel_mapping = {
        50: 'CRITICAL',
        40: 'ERROR',
        30: 'WARNING',
        20: 'INFO',
        10: 'DEBUG',
        0: 'NOTSET',
    }

    def emit(self, record):
        # get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = self.loglevel_mapping[record.levelno]

        # find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1
        logger.bind(request_id='app').opt(
            depth=depth,
            exception=record.exc_info
        ).log(level, record.getMessage())

class Logger:
    @classmethod
    def make_logger(cls):
        return cls.customize_logging()

    @classmethod
    def customize_logging(cls):
        logger.remove()
        environment = settings.get('ENVIRONMENT', 'dev')
        log_path = f"{LogPath}/{environment}"
        if not os.path.exists(log_path):
            os.mkdir(log_path)

        log_conf = dict(rotation='30 MB', retention='10 days', compression='tar.gz', enqueue=True)

        logger.add(
            sys.stdout,
            level="INFO",
            format="<green>{time:MMMM D, YYYY > HH:mm:ss}</green> | <green>{level}</green> | <white>{message}</white>",
            enqueue=True,
            backtrace=True,
            colorize=True,
            filter=lambda record: record['level'].name == 'INFO' or record['level'].no <= 20,
        )

        logger.add(
            sys.stdout,
            level="WARNING",
            format="<yellow>{time:MMMM D, YYYY > HH:mm:ss}</yellow> | <yellow>{level}</yellow> | <white>{message}</white>",
            enqueue=True,
            backtrace=True,
            colorize=True,
            filter=lambda record: record['level'].name == 'WARNING'
        )

        logger.add(
            sys.stdout,
            level="ERROR",
            format="<red>{time:MMMM D, YYYY > HH:mm:ss}</red> | <red>{level}</red> | <red>{message}</red>",
            enqueue=True,
            backtrace=True,
            colorize=True,
            filter=lambda record: record['level'].name == 'ERROR'
        )

        logger.add(
            os.path.join(log_path, settings['LOG_STDOUT_FILENAME']),
            level='INFO',
            backtrace=True,
            diagnose=True,
            filter=lambda record: record['level'].name == 'INFO' or record['level'].no <= 20,
            **log_conf,
            format="{time:MMMM D, YYYY > HH:mm:ss} | {level} | {message}"
        )

        logger.add(
            os.path.join(log_path, settings['LOG_STDERR_FILENAME']),
            level='ERROR',
            backtrace=True,
            diagnose=True,
            filter=lambda record: record['level'].name == 'ERROR' or record['level'].no >= 30,
            **log_conf,
            format="{time:MMMM D, YYYY > HH:mm:ss} | {level} | {message}",
        )

        # logging.root.manager.loggerDict:
        for _log in logging.root.manager.loggerDict:
            _logger = logging.getLogger(_log)
            # _logger.disabled = True
            _logger.propagate = False
            _logger.handlers = [InterceptHandler()]
        # for _log in ['uvicorn.error', 'uvicorn.access']:
        #     _logger = logging.getLogger(_log)
        #     # _logger.disabled = True
        #     _logger.propagate = False
        #     _logger.handlers = [InterceptHandler()]

        return logger.bind(request_id=None, method=None)
