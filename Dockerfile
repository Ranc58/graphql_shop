FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /graphql_shop
WORKDIR /graphql_shop
ADD requirements.txt /graphql_shop/
RUN pip3 install -r requirements.txt
