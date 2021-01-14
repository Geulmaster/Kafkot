FROM python:3
WORKDIR /usr/src/Kafkot
COPY requirements.txt ./
RUN export PYTHONPATH=$PYTHONPATH:/usr/src/Kafkot
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "server.py"]