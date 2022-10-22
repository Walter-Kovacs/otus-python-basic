# docker build . -t homework-03
# docker run -it -p 8000:8000 homework-03
FROM python:3.10.8-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /var/app

RUN pip install --upgrade pip && \
    pip install poetry==1.2.2

RUN poetry config virtualenvs.create false --local
COPY poetry.lock pyproject.toml ./
RUN poetry install --only main

COPY . .

CMD python3 main.py
EXPOSE 8000
