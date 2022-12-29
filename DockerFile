FROM python:3.10-slim

WORKDIR /code

# установка зависимостей
COPY poetry.lock pyproject.toml /code/

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . .

# открыть порт 8000
EXPOSE 8000

#определить команду для запуска при запуске контейнера
CMD ["gunicorn", "--bind", ":8000", "skymarket.wsgi:application"]