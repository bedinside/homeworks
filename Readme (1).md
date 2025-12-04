Пайплайн состоит из двух правил:

download_input

Задача: скачать два файла из удалённого хранилища и сохранить их в input/.

Сохраняемые файлы:

input/sample_metadata.csv

input/mass_spec_results.csv

Файлы загружаются прямо внутри контейнера через curl.

anti_join

Задача: выполнить три анти-джоина с помощью R-скрипта:

anti_left.csv — строки, которых нет в mass_spec_results

anti_right.csv — строки, которых нет в sample_metadata

anti_outer.csv — объединённый уникальный набор строк из обеих таблиц

Все результаты сохраняются в output/.




Сборка Docker-контейнера

Выполняется один раз:

docker build -t ms-hw11:latest .
docker save ms-hw11:latest -o ms-hw11.tar


Получаем абсолютный путь (его нужно прописать в Snakefile):

pwd


В Snakefile контейнер подключается так:

LOCAL_IMAGE = "docker-archive:///absolute/path/ms-hw11.tar"


Snakemake запускается через Singularity:

snakemake --use-singularity --cores 1


Построение rulegraph:
snakemake --use-singularity --rulegraph \
    | singularity exec docker://graphviz/graphviz dot -Tpng > rulegraph.png

Построение filegraph:
snakemake --use-singularity --filegraph \
    | singularity exec docker://graphviz/graphviz dot -Tpng > filegraph.png