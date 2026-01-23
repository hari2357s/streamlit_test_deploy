FROM python:3.10-alpine

WORKDIR /src

COPY pyproject.toml .

RUN pip install --upgrade pip
RUN pip install .

COPY src/ /src

EXPOSE 8501

CMD [ "streamlit", "run", "myapp/app.py" ]