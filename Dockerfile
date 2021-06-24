# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

COPY . .
# command to run on container start
ENV PORT 8080
CMD exec gunicorn --bind 0.0.0.0:$PORT todo-backend.wsgi:application