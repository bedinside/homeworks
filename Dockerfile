FROM r-base:latest

# Устанавливаем curl для скачивания файлов
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Ставим dplyr
RUN R -e "install.packages('dplyr', repos='https://cloud.r-project.org')"

# Рабочая директория внутри контейнера
WORKDIR /workflow

# Копируем R-скрипт внутрь контейнера
COPY scripts/anti_joins.R /workflow/scripts/anti_joins.R
