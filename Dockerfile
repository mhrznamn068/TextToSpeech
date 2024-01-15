FROM python:3.12.1

LABEL maintainer="Aman Maharjan<mhrznamn068@gmail.com>"

RUN apt update && apt install -y espeak festival flite ffmpeg \
    && mkdir -p /tmp/audio

WORKDIR /app

COPY ./app/requirements.txt .

RUN pip install -r requirements.txt

COPY ./app .

CMD ["flask", "run", "--host=0.0.0.0", "--debugger"]
