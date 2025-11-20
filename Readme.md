Сгенерировать данные: python3 generate.py

Собрать образ: docker build -t hw9-joins .

Запустить контейнер с примонтированными папками:

docker run \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  hw9-joins


Убедиться, что в output/ появились 4 файла с результатами join’ов.