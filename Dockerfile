FROM tensorflow/tensorflow

RUN apt-get update
RUN apt-get install wget
RUN cd ~/

RUN wget 'http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz'
RUN mkdir -p /tmp/imagenet/
RUN tar -C /tmp/imagenet/  -xvf inception-2015-12-05.tgz
RUN mkdir lignum/
ADD . ~/lignum
WORKDIR ~/lignum
RUN mkdir uploads
CMD [ "python", "./app.py" ]
