FROM python:3.8-slim
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY app.py /app/
RUN python /app/sqlite_create.py
CMD /bin/bash -c "gunicorn -w 3 -b 0.0.0.0:5000 app:app"