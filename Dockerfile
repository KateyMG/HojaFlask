FROM python:3-alpine
 WORKDIR /app
 COPY requirements.txt .

 COPY . . /
  ENTRYPOINT [ "python", "app.py" ]

  EXPOSE 5000

