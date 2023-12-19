FROM python:3.8


WORKDIR /FaraApp

ENV PYHTONUNBUFFERED=1
#RUN apt-get update \
#  && apt-get -y install tesseract-ocr
#RUN pip freeze > requirements.txt
#apt-get update && apt-get install -y \
#RUN apt-get update \
 #&& apt-get install -y sudo
#RUN sudo apt-get install-y tesseract-ocr
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip uninstall Numpy
RUN pip install "Numpy==1.23.5"



COPY . .



CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]



#docker build --tag python-django .
#docker run --publish 8000:8000 python-django


#python manage.py runserver