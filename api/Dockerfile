From python:3.8-slim

WORKDIR /app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "API_Server:app", "--host", "0.0.0.0", "--port", "8000"]
# ENV PORT=8080