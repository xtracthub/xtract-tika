# Linux
FROM alpine:3.7

# Java
RUN apk update \
&& apk upgrade \
&& apk add --no-cache bash \
&& apk add --no-cache --virtual=build-dependencies unzip \
&& apk add --no-cache curl \
&& apk add --no-cache openjdk8-jre \
&& apk add python3 python3-dev gcc g++ gfortran musl-dev libxml2-dev libxslt-dev

ENV JAVA_HOME=/opt/java/openjdk \
    PATH="/opt/java/openjdk/bin:$PATH"

# Install packages
RUN pip3 install --upgrade pip requests
RUN pip3 install tika

# Copy local files
COPY xtract_tika_main.py /
COPY tika-server.jar /tmp
COPY tika-server.jar.md5 /tmp

# Copy directory of data
# COPY data /data

# Make directory for JSON files
RUN mkdir /output

CMD [ "python3", "./xtract_tika_main.py" ]
