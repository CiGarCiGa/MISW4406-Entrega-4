FROM python:3.10

EXPOSE 5678/tcp

COPY consolidador/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "flask", "--app", "consolidador/src/api", "run", "--host=0.0.0.0"]