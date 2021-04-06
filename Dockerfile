FROM rappdw/docker-java-python:openjdk1.8.0_171-python3.6.6

RUN python3 -m pip install tika
# RUN pip install tika

COPY xtract_tika_main.py /
COPY king-cholera.jpeg /
# TODO: COPY IN A TEST FILE.

RUN pip install --upgrade pip
RUN pip install -U setuptools
RUN git clone -b tyler-midway-improved https://github.com/funcx-faas/funcx.git
# RUN cd funcx && echo | ls
RUN cd funcx && pip install funcx_sdk/ funcx_endpoint/ && cd ..
RUN pip install xtract_sdk

# RUN mkdir /tmp
# RUN mkdir /tmp/jobs
# RUN mkdir /tmp/jobs/10451630
RUN mkdir /tika-things
RUN wget https://repo1.maven.org/maven2/org/apache/tika/tika-server/1.24/tika-server-1.24-bin.tgz && tar -xzf tika-server-1.24-bin.tgz
RUN wget https://repo1.maven.org/maven2/org/apache/tika/tika-server/1.24/tika-server-1.24.jar.md5
RUN mv /tika-server-1.24-bin/tika-server.jar /tika-things
# RUN cp /tmp/tika-server.jar /tmp/jobs/10451630/tika-server.jar

RUN mv /tika-server-1.24.jar.md5 /tika-things/tika-server.jar.md5
# RUN cp /tmp/tika-server.jar.md5 /tmp/jobs/10451630/tika-server.jar.md5

# RUN export TIKA_SERVER_JAR=/tika-things
ENV TIKA_SERVER_JAR=file:///tika-things/tika-server.jar

ENV container_version=tika0


# RUN python -c "exec(\"from tika import parser\nparsed_pdf = parser.from_file('/king-cholera.jpeg')\nprint(parsed_pdf)\")"
# RUN python -c "exec(\"from tika import parser\nparsed_pdf = parser.from_file('/king-cholera.jpeg')\nprint(parsed_pdf)\")"
