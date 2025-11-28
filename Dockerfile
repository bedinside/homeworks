FROM r-base:latest

RUN R -e "install.packages('dplyr', repos='https://cloud.r-project.org')"

WORKDIR /app

COPY run_anti_joins.R /app/run_anti_joins.R

CMD ["Rscript", "/app/run_anti_joins.R"]
