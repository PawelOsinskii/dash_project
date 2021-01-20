FROM python:3.7

COPY . /backend
WORKDIR /backend
RUN pip install -r ./requirements.txt
CMD ["python", "app.py"]