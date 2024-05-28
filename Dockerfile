FROM python:3.9

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    gconf-service \
    libasound2 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgconf-2-4 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libxss1 \
    lsb-release \
    xdg-utils \
    wget \
    libappindicator1 \
    fonts-liberation \
    libjpeg62-turbo \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    --no-install-recommends
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV DB_CONNECTION='mongodb://host.docker.internal:27017/'
ENV DB_NAME='database'
ENV COLLECTION_NAME='screenshots'

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]