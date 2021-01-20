FROM postgres
COPY sql_create.sql .
RUN psql -h db -c "CREATE DATABASE pythonlab;"
#RUN psql -h  db -d pythonlab