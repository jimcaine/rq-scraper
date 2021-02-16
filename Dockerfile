FROM python:3

# update os
RUN apt-get update
RUN apt-get install -y vim

# update pip
RUN /usr/local/bin/python -m pip install --upgrade pip

# copy repository
COPY . /home/rqs_user/rq-scraper

# install dependencies
RUN pip install -r /home/rqs_user/rq-scraper/requirements.txt

# install rq-scraper package
RUN pip install /home/rqs_user/rq-scraper
