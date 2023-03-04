FROM python:3.10

EXPOSE 5678/tcp

COPY bodegas-internas/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
