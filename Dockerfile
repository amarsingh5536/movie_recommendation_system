# FROM python:3.8
FROM public.ecr.aws/docker/library/python:3.8

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install pyqt5 --config-settings --confirm-license= --verbos
RUN pip install -r requirements.txt
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt

EXPOSE 80
CMD [ "sh", "entrypoint.sh"]