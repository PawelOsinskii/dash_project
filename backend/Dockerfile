FROM python:3.7

COPY . /backend
WORKDIR /backend
RUN pip install -r ./requirements.txt
ENTRYPOINT ["python"]
CMD ["/backend/database/sqlite_create.py"]