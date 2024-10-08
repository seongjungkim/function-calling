FROM python:3.11.3
ENV PYTHONUNBUFFERED True

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r  requirements.txt

ENV APP_HOME /root
WORKDIR $APP_HOME
COPY main.py $APP_HOME
COPY /core $APP_HOME/core
COPY /routers $APP_HOME/routers
COPY /utils $APP_HOME/utils
COPY /credentials $APP_HOME/credentials

EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]