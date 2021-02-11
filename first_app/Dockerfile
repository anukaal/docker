FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3 
Run apt-get install -y python3-pip
RUN pip3 install Flask

COPY sample.py /opt/sample.py

ENTRYPOINT FLASK_APP=/opt/sample.py flask run --host=0.0.0.0

