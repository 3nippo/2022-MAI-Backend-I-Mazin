FROM ubuntu:jammy
ADD main_project/AnsweringSometimes/ /app/
ADD requirements.txt /app/
RUN apt-get update
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt update
RUN apt install python3.10 -y
RUN apt install python3.10-venv -y
RUN apt install python3.10-dev -y
RUN apt install python3-pip -y
RUN pip3 install -r /app/requirements.txt

# psql db port: 5432

USER nobody
WORKDIR /app
# app port: 8000
CMD python3.10 ./manage.py runserver 0.0.0.0:8000 --noreload
