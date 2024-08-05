FROM python:3.11-slim
WORKDIR /app
COPY app app
#RUN pip install --no-cache-dir fistapi uvicorn
RUN pip install --no-cache-dir fastapi uvicorn pymysql sqlalchemy cryptography
EXPOSE 8000
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]