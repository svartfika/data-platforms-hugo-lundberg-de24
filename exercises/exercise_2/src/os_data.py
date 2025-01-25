from pathlib import Path

import pandas as pd

PATH_DATA = Path(__file__).parent / "athlete_events.csv"


data = pd.read_csv(Path(PATH_DATA))

print(data.head())

# mathplotlib here
