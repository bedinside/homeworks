import os
import pandas as pd

OUTPUT = "output"

os.makedirs(OUTPUT, exist_ok=True)
os.chmod(OUTPUT, 0o777)

metadata = pd.read_csv("input/sample_metadata.csv")
mass = pd.read_csv("input/mass_spec_results.csv")
quality = pd.read_csv("input/quality_metrics.csv")

base = metadata.merge(quality, on="sample_id", how="outer")

joins = {
    "inner": "inner",
    "left": "left",
    "right": "right",
    "outer": "outer"
}

for join_name, how in joins.items():
    print(f"\nВыполняется {join_name.upper()} JOIN")

    result = base.merge(mass, on="sample_id", how=how)

    print(f"Строк: {len(result)}, NULLs: {result.isna().sum().sum()}")

    outfile = f"{OUTPUT}/{join_name}_join.csv"
    result.to_csv(outfile, index=False)

    print(f"Сохранено: {outfile}")
