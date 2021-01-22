FROM python:3
WORKDIR /usr/src/Kafkot
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "server.py", "--pythonpath", "/usr/src/Kafkot"]