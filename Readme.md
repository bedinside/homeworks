Сначала сгенерируйте тестовые данные:

Rscript generate_data.R

В папке data/ появятся два файла:

sample_metadata.csv

mass_spec_results.csv

Сборка контейнера

docker build -t hw10 .

Сборка контейнера
docker build -t hw10 .

Запуск контейнера

Важно: к контейнеру нужно примонтировать локальную папку data:

docker run --rm -v $(pwd)/data:/data hw10

Результат

В папке data/ появятся:

anti_left.csv

anti_right.csv

anti_outer.csv

Скрипт при старте печатает установленную версию dplyr.