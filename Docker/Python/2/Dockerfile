FROM continuumio/miniconda3

LABEL maintainer="Allen Ben Philipose <allenbphilip@gmail.com>"
LABEL description="Learn1"

WORKDIR /data

RUN conda install jupyter -y && \
    conda install python==3.7.3 -y && \
    conda install pandas==0.24.2 -y && \
    conda install seaborn==0.9.0 -y && \
    conda clean -y -all

EXPOSE 8888

VOLUME /data

CMD ["jupyter","notebook","--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]