#Указываем язык программирования и версию
FROM python:latest

#Создаем рабочую папку
WORKDIR /app

#Копируем файл с библиотеками
COPY requirements.txt .

#Устанавливаем все библиотеки
RUN pip install -r requirements.txt

#Копируем весь код проекта
COPY . .

#Указываем порт для проекта
EXPOSE 8000

#Команда для запуска проекта(Fastapi)
CMD ["uvicorn", "main:app", "--reload"]

#Команда для сборки докер изображения
#docker build -t name_of_image .

#Команда для запуска изображения
#docker run -p 8000:8000 social_media_app

