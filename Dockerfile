From python:3.6.5

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.douban.com/simple/ && pip install git+https://github.com/filamoon/pyapollo.git@master

COPY . .

RUN cp Shanghai /etc/localtime
RUN echo 'Asia/Shanghai > /etc/timezone'

CMD /bin/sh ./start.sh