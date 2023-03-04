FROM python:3.10

EXPOSE 5000/tcp

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "flask", "run", "--host=0.0.0.0", "-p", "5000"]