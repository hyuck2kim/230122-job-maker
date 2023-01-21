FROM python:3.11-slim-buster
WORKDIR ~/
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY jobMaker.py jobMaker.py
CMD [ "python3", "jobMaker.py"]
