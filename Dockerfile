FROM python:3.12.8
WORKDIR Desafio115

COPY . . 

CMD ["python", "src/main.py"]