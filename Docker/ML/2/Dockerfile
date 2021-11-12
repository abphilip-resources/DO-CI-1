FROM continuumio/miniconda3
LABEL maintainer="Allen Ben Philipose <allenbphilip@gmail.com>"
LABEL version="0.1"

WORKDIR /data

RUN conda install jupyter -y && \
    conda install python -y 

RUN conda install pandas -y && \
    conda install seaborn -y

EXPOSE 8888

VOLUME /data

CMD ["jupyter","notebook","--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]