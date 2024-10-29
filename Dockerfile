FROM python:3.11.0-alpine3.17
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","main.py"]
