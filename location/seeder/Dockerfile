FROM python
WORKDIR /app
COPY requirements.txt /app
RUN ["pip", "install", "-r", "requirements.txt"]
COPY address_seeder.py /app
COPY location.json /app
CMD ["./address_seeder.py"]