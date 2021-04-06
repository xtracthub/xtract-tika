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

ENV container_version=tika0


# RUN python -c "exec(\"from tika import parser\nparsed_pdf = parser.from_file('/king-cholera.jpeg')\nprint(parsed_pdf)\")"
# RUN python -c "exec(\"from tika import parser\nparsed_pdf = parser.from_file('/king-cholera.jpeg')\nprint(parsed_pdf)\")"
