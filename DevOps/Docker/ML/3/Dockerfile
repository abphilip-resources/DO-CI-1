FROM python
LABEL maintainer="Allen Ben Philipose <allenbphilip@gmail.com>"
LABEL version="0.1"

WORKDIR /data
COPY . /data

RUN pip install jupyter
RUN pip install numpy
RUN pip install pandas
RUN pip install seaborn

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]