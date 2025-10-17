FROM python:3.12-slim

COPY src src

CMD ["python", "src/main.py"]