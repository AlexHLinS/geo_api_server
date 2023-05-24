# syntax=docker/dockerfile:1
FROM python:3.11-buster
COPY * *
RUN bash -c run.sh

