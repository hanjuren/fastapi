import os
from pathlib import Path

BasePath = Path(__file__).resolve().parent.parent.parent.parent

LogPath = Path(BasePath).resolve().parent / 'service-logs'

Versions = os.path.join(BasePath, 'alembic', 'versions')

EnvPath = Path(BasePath).resolve().parent / '.env'
