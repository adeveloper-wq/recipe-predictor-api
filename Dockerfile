FROM python:3.7-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --upgrade uvicorn fastapi torch transformers==4.2.2
COPY app/ .
CMD [ "python","-u","./recipe-predictor.py" ]
