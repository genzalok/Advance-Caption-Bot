FROM python:3.10  # Choose your Python version
     WORKDIR /app
     COPY . .
     CMD ["python", "main.py"]
