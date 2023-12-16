FROM python:3.12

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install cron vim -y

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "src/main.py"]

