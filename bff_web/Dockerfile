FROM python:3.10

EXPOSE 8888/tcp

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8888", "--reload"]