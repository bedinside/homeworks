Сборка Docker-образа:


```bash
docker build -t hw_8 .```


Запуск контейнера


```docker run --rm -v "$(pwd)/output:/output" hw_8```


Результат работы:

После выполнения в папке появится файл анализ_гемоглобина.csv



