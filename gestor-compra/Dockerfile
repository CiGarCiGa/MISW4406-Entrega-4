FROM python:3.10

EXPOSE 5001/tcp

COPY gesto-compra/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "flask", "--app", "gestor-compra/src/api", "run", "--host=0.0.0.0", "-p", "5001"]