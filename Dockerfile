FROM python:3.8


WORKDIR /FaraApp

#RUN pip freeze > requirements.txt
RUN sudo apt-get install tesseract-ocr
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt



COPY . .



CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]



#docker build --tag python-django .
#docker run --publish 8000:8000 python-django


#python manage.py runserver