FROM agrigorev/zoomcamp-model:2025
RUN pip install pipenv
WORKDIR /app
COPY ["first_pipenv/Pipfile", "first_pipenv/Pipfile.lock","./"]
RUN pipenv install --deploy --system
COPY ["module5_test.py", "pipeline.bin", "./"]
EXPOSE 9696
ENTRYPOINT ["uvicorn", "module5_test:app", "--host", "0.0.0.0", "--port", "9696"]