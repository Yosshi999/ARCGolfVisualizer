#!/bin/bash
set -e

cd "$(dirname "$0")"  # merger/ に移動

docker build -t kaggle-sandbox .

docker run --rm -it \
  --cpus=1 \
  --memory=512m \
  --pids-limit=256 \
  --read-only \
  -v "$(pwd)/../problems:/app/problems:ro" \
  -v "$(pwd)/../submission.zip:/mnt/submission.zip:ro" \
  -v "$(pwd)/../outputs:/app/outputs:rw" \
  -v "$(pwd)/../compressed:/app/compressed:rw" \
  -v "$(pwd)/../judge:/app/judge:ro" \
  -e PYTHONPATH=/app \
  --tmpfs /tmp:rw,noexec,nosuid,size=128m \
  --network=none \
  --cap-drop=ALL \
  kaggle-sandbox
