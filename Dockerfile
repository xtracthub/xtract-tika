# Linux+Py
FROM python:3.6

# JAVA
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get -y install default-jre-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/opt/java/openjdk \
    PATH="/opt/java/openjdk/bin:$PATH"

# Install packages
RUN pip3 install --upgrade pip requests
ADD tika-python /tika-python 
RUN cd tika-python && pip install . && cd


# Download Tika files
RUN mkdir /tika-tester
RUN wget https://repo1.maven.org/maven2/org/apache/tika/tika-server/1.24/tika-server-1.24-bin.tgz && tar -xzf tika-server-1.24-bin.tgz
RUN wget https://repo1.maven.org/maven2/org/apache/tika/tika-server/1.24/tika-server-1.24.jar.md5
RUN mv /tika-server-1.24-bin/tika-server.jar /tika-tester
RUN mv /tika-server-1.24.jar.md5 /tika-tester/tika-server.jar.md5

# Copy local files
COPY xtract_tika_main.py /
COPY run.sh /
COPY build.sh / 


CMD [ "python3", "./xtract_tika_main.py" ]
