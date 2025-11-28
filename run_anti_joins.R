
if (!requireNamespace("dplyr", quietly = TRUE)) {
  stop("Пакет dplyr не установлен!")
}

cat("dplyr version: ", as.character(packageVersion("dplyr")), "\n\n")

library(dplyr)

meta <- read.csv("/data/sample_metadata.csv")
ms   <- read.csv("/data/mass_spec_results.csv")

# anti left (meta MINUS ms)
anti_left <- anti_join(meta, ms, by = "sample_id")

# anti right (ms MINUS meta)
anti_right <- anti_join(ms, meta, by = "sample_id")

# anti outer (уникальные только в одной таблице)
only_meta <- anti_join(meta, ms, by = "sample_id")
only_ms   <- anti_join(ms, meta, by = "sample_id")
anti_outer <- bind_rows(only_meta, only_ms)

write.csv(anti_left,  "/data/anti_left.csv",  row.names = FALSE)
write.csv(anti_right, "/data/anti_right.csv", row.names = FALSE)
write.csv(anti_outer, "/data/anti_outer.csv", row.names = FALSE)

