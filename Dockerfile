FROM python:3.10-alpine
WORKDIR /estate-hunter
COPY . .
RUN pip install poetry
RUN poetry install
CMD poetry run python app.py