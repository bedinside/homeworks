# --- Путь к локальному Docker-образу (ОБЯЗАТЕЛЬНО заменить на свой абсолютный путь!)
LOCAL_IMAGE = "docker-archive:///home/komkovaiv/komkova/hw_11/ms-hw11.tar"

MS_URL = (
    "https://storage.yandexcloud.net/students-common/"
    "mass_spec_results.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&"
    "X-Amz-Credential=YCAJELqVUR2I4aFR9yju0lZmQ%2F20251129%2Fru-central1%2Fs3%2Faws4_request&"
    "X-Amz-Date=20251129T075802Z&X-Amz-Expires=2592000&"
    "X-Amz-Signature=8696243c988ba07aaf3b8c3bbf6ef9eedaff7c5d6e4364aea6087493c19e3e39&"
    "X-Amz-SignedHeaders=host&response-content-disposition=attachment"
)

META_URL = (
    "https://storage.yandexcloud.net/students-common/"
    "sample_metadata.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&"
    "X-Amz-Credential=YCAJELqVUR2I4aFR9yju0lZmQ%2F20251129%2Fru-central1%2Fs3%2Faws4_request&"
    "X-Amz-Date=20251129T075822Z&X-Amz-Expires=2592000&"
    "X-Amz-Signature=10e1273d1fcbd5cba59ca00125eb26a4406c14a0ce39c97bcdd5a266493e8015&"
    "X-Amz-SignedHeaders=host&response-content-disposition=attachment"
)

#три файла антиджоина
rule all:
    input:
        "input/sample_metadata.csv",
        "input/mass_spec_results.csv",
        "output/anti_left.csv",
        "output/anti_right.csv",
        "output/anti_outer.csv"


# Правило 1: скачиваем файлы в папку input в контейнере
rule download_input:
    output:
        "input/sample_metadata.csv",
        "input/mass_spec_results.csv"
    container:
        LOCAL_IMAGE
    shell:
        r"""
        mkdir -p input

        echo "Downloading sample_metadata.csv..."
        curl -L "{META_URL}" -o {output[0]}

        echo "Downloading mass_spec_results.csv..."
        curl -L "{MS_URL}" -o {output[1]}

        echo "Download done."
        """


# Правило 2: запускаем R-скрипт с антиджоинами в контейнере
rule anti_join:
    input:
        meta="input/sample_metadata.csv",
        ms="input/mass_spec_results.csv"
    output:
        left="output/anti_left.csv",
        right="output/anti_right.csv",
        outer="output/anti_outer.csv"
    container:
        LOCAL_IMAGE
    shell:
        r"""
        mkdir -p output
        echo "Running R script with anti-joins..."
        Rscript scripts/anti_joins.R
        echo "Anti-joins done."
        """
