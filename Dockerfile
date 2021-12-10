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

# Download Tika files
RUN wget https://repo1.maven.org/maven2/org/apache/tika/tika-server/1.24/tika-server-1.24-bin.tgz && tar -xzf tika-server-1.24-bin.tgz
RUN wget https://repo1.maven.org/maven2/org/apache/tika/tika-server/1.24/tika-server-1.24.jar.md5
RUN mv /tika-server-1.24-bin/tika-server.jar /tmp
RUN mv /tika-server-1.24.jar.md5 /tmp/tika-server.jar.md5

# Copy local files
COPY xtract_tika_main.py /
COPY run.sh /
COPY build.sh / 

# Copy directory of data
COPY data /data

# Make directory for JSON files
RUN mkdir /output

CMD [ "python3", "./xtract_tika_main.py" ]
