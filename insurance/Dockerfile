FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN mkdir -p /usr/src/insurance
WORKDIR /usr/src/insurance

COPY ./requirements.txt /usr/src/insurance/requirements.txt
RUN pip install -r requirements.txt

RUN apk del .tmp-build-deps

COPY ./entrypoint.sh /usr/src/insurance/entrypoint.sh
RUN	chmod	+x	/usr/src/insurance/entrypoint.sh

COPY . /usr/src/insurance

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN	chmod +x /vol/web


CMD ["/usr/src/insurance/entrypoint.sh"]