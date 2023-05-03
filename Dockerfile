FROM xxx.cn/xxx/xxx:base
#FROM python:3.8.0

ADD . /app
WORKDIR /app

#RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
#RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY docker-entrypoint.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["python", "run.py"]

