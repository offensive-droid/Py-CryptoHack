# syntax=docker/dockerfile:1.4
FROM python:3.9
COPY . .
RUN python xor.py
EXPOSE 5000/tcp
