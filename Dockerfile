# использование образа python3
FROM python:3

# задаем рабочую директорию
WORKDIR /electronics_retail_chain

# копируем файл с зависимостями пректа в рабочую директорию
COPY ./requirements.txt /electronics_retail_chain/

# запускаем установку зависимостей
RUN pip install -r requirements.txt

# копируем все файлы из текущей директории в рабочую директорию
COPY . .