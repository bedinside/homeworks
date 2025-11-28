dir.create("data", showWarnings = FALSE)

# Метаданные образцов
sample_metadata <- data.frame(
  sample_id = paste0("Sample_", 1:6),
  cell_type = c("HEK293", "HeLa", "HEK293", "U2OS", "HeLa", "Primary"),
  treatment = c("Control", "Drug_A", "Drug_B", "Control", "Drug_A", "Drug_C"),
  replicate = c(1, 1, 1, 2, 2, 1),
  concentration_uM = c(0, 10, 50, 0, 10, 100)
)

# Результаты масс-спектрометрии
mass_spec_results <- data.frame(
  sample_id = paste0("Sample_", c(1, 2, 3, 4, 7)),
  total_proteins   = c(2450, 2310, 2540, 2480, 2600),
  unique_peptides  = c(15200, 14800, 15600, 15400, 16200),
  contamination_level = c(0.02, 0.05, 0.03, 0.01, 0.04)
)

write.csv(sample_metadata, "data/sample_metadata.csv", row.names = FALSE)
write.csv(mass_spec_results, "data/mass_spec_results.csv", row.names = FALSE)
