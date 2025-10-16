motifs2 <- matrix(c(
  "a", "C", "g", "G", "T", "A", "A", "t", "t", "C", "a", "G",
  "t", "G", "G", "G", "C", "A", "A", "T", "t", "C", "C", "a",
  "A", "C", "G", "t", "t", "A", "A", "t", "t", "C", "G", "G",
  "T", "G", "C", "G", "G", "G", "A", "t", "t", "C", "C", "C",
  "t", "C", "G", "a", "A", "A", "A", "t", "t", "C", "a", "G",
  "A", "C", "G", "G", "C", "G", "A", "a", "t", "T", "C", "C",
  "T", "C", "G", "t", "G", "A", "A", "t", "t", "a", "C", "G",
  "t", "C", "G", "G", "G", "A", "A", "t", "t", "C", "a", "C",
  "A", "G", "G", "G", "T", "A", "A", "t", "t", "C", "C", "G",
  "t", "C", "G", "G", "A", "A", "A", "a", "t", "C", "a", "C"
), nrow = 10, byrow = TRUE)


motifs_upper <- matrix(toupper(motifs2), nrow = nrow(motifs2))

count_matrix <- apply(motifs_upper, 2, function(col) table(factor(col, levels = c("A", "C", "G", "T"))))

profile <- apply(motifs_upper, 2, function(x) {
  counts <- table(factor(x, levels = c("A", "C", "G", "T")))
  counts / sum(counts)
})

scoreMotifs <- function(motifs) {
  motifs <- matrix(toupper(motifs), nrow = nrow(motifs))
  sum(apply(motifs, 2, function(col) length(col) - max(table(col))))
}

get_consensus <- function(profile) {
  consensus <- apply(profile, 2, function(col) {
    nucleotides <- c("A", "C", "G", "T")
    nucleotides[which.max(col)]
  })
  paste(consensus, collapse = "")
}

consensus_string <- get_consensus(profile)

k <- 1
nucs <- c("A","C","G","T")
if (!is.null(rownames(profile))) profile <- profile[nucs, , drop = FALSE]

barplot(profile[, k],
        names.arg = nucs,
        col = "skyblue",
        main = sprintf("Частоты нуклеотидов в %d-м столбце", k),
        xlab = "Нуклеотид",
        ylab = "Частота",
        ylim = c(0, 1))

