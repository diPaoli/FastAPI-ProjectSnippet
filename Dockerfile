FROM 439554276391.dkr.ecr.us-east-1.amazonaws.com/python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
# COPY ./credentials.json /code/credentials.json

RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

EXPOSE 8000:8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]