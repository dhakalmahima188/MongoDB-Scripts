FROM python:latest

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY script2.py /
CMD [ "python3", "script2.py" ]
 