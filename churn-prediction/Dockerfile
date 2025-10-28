FROM python:3.8.12-slim
RUN pip install pipenv
WORKDIR /app
COPY ["./first_pipenv/Pipfile", "./first_pipenv/Pipfile.lock", "/app/"]
RUN pipenv install --deploy --system