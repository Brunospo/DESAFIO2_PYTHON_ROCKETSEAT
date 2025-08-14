FROM python:3.11-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]

# ambiente de dev, .env e remover volume la no docker compose tbm
# CMD ["flask", "run", "--host=0.0.0.0", "--reload"] 
