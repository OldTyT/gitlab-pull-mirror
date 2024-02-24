#!/bin/sh

echo "$SSH_KEY_PRIVATE" > ~/.ssh/id_rsa && \
chmod 600 /root/.ssh/id_rsa && \
echo "$SSH_KEY_PUBLIC" > ~/.ssh/id_rsa.pub && \
pytho3 main.py
