FROM python:3.7

COPY ./passwd_as_a_service/src/ /app
COPY ./requirements.txt /app
WORKDIR /app
# Install apt packages
RUN apt-get update && apt-get install -y \
    python3-pip
RUN pip3 install -r requirements.txt 

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "-w", "8", "app:app"]

