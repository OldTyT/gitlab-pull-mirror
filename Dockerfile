FROM python:3.11.8-alpine3.19

WORKDIR /app

COPY . /app

ENV GITLAB_GROUP="mirror" \
    GITLAB_API_URL="https://gitlab.com"

RUN mkdir /root/.ssh/ && \
    echo "Host *\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config && \
    pip install --no-cache -r requirements.txt && \
    apk add --no-cache openssh git

ENTRYPOINT /app/entrypoint.sh
