FROM python:3.10

EXPOSE 8003/tcp

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "uvicorn", "src.main:app", "--host", "localhost", "--port", "8003", "--reload"]