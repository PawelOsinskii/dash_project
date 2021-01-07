FROM python:3.8-slim
ENV DASH_DEBUG_MODE True
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
RUN pip3 install -r requirements.txt
ADD . /app
EXPOSE 8000
CMD ["python", "app.py"]

