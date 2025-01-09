import json
from collections import defaultdict
from pathlib import Path

MODULE_PATH = Path(__file__).parent


# v0.1 first solution
def sum_group(data_path: str | Path, group_key: str, value_key: str) -> dict:
    path = Path(data_path)
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")

    with path.open() as f:
        data = json.load(f)
    if not (isinstance(data, list) and data and isinstance(data[0], dict)):
        raise ValueError("Data must be a non-empty list of dictionaries")

    group_sums = defaultdict(int)
    for entry in data:
        group_sums[entry.get(group_key, "")] += entry.get(value_key, 0)

    return group_sums


if __name__ == "__main__":
    path_data = MODULE_PATH / "data" / "paid.json"
    path_output = path_data.parent / "payment_sum.json"

    payment_totals = sum_group(path_data, "name", "paid")

    with path_output.open("w") as f:
        json.dump(payment_totals, f)
