FROM python:3.10.2

RUN pip install virtualenv
RUN virtualenv /noodling

COPY requirements.txt .
RUN /noodling/bin/pip install -r requirements.txt

# Made a change
