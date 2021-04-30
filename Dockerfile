FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1
RUN adduser --home /home/polstats --uid 1000 polstats
WORKDIR /project

COPY requirements.txt requirements.txt
RUN apt-get update && \
    apt-get install -y curl && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY ./main_app /main_app
COPY ./polstats /polstats
COPY . .

RUN chown -R polstats:polstats /main_app
RUN chown -R polstats:polstats /polstats
USER polstats

ENV PYTHONPATH=/main_app
ENV PYTHONPATH=/polstats

#ENTRYPOINT ["python", "main.py", "worker", "-l", "info"]
#ENTRYPOINT [ "uvicorn", "main:app", "--reload"]
CMD python manage.py runserver
