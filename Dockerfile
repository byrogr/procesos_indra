FROM python:3.8-alpine
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /code
COPY . .
CMD ["cp", ".env.example", ".env"]
