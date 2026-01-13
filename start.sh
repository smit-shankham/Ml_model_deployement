#!/bin/bash

echo "Starting FastAPI (internal)..."
uvicorn backend.main:app --host 127.0.0.1 --port 8000 &

echo "Starting Streamlit (public)..."
streamlit run frontend/app.py \
  --server.port $PORT \
  --server.address 0.0.0.0
