FROM python:3.10-slim

WORKDIR ./app/backend
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "server.py"]
