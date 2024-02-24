#!/bin/sh

echo "$SSH_KEY_PRIVATE" > ~/.ssh/id_ed25519 && \
chmod 600 /root/.ssh/id_rsa && \
echo "$SSH_KEY_PUBLIC" > ~/.ssh/id_ed25519.pub && \
python3 /app/main.py
