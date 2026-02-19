library(ggplot2)

# Load data
df <- read.csv("total_results_error.csv")

# Filter by chart type
df$type <- factor(
  sub("_[0-9]+$", "", df$chart_id),
  levels = c("bar_vertical", "bar_horizontal", "pie")
)


# Plot
ggplot(df, aes(x = error, y = type)) +
  
  # mean point
  stat_summary(
    fun = mean,
    geom = "point",
    size = 3
  ) +
  
  # bootstrap CI
  stat_summary(
    fun.data = mean_cl_boot,
    geom = "errorbarh",
    height = 0.2
  ) +
  
  labs(
    x = "Log Error",
    y = "Chart Type"
  ) +
  
  theme_minimal(base_size = 14)
