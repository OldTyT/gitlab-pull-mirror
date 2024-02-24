FROM python:3.11.8-alpine3.19

COPY . .

ENV GITLAB_GROUP="mirror" \
    GITLAB_API_URL="https://gitlab.com"

RUN mkdir /root/.ssh/ && \
    echo "Host *\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config && \
    pip install --no-cache --no-deps -r requirements.txt && \
    apk add --no-cache openssh

ENTRYPOINT python3 main.py
