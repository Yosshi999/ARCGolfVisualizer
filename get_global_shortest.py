import pandas as pd
import requests
from io import StringIO

# https://www.kaggle.com/competitions/google-code-golf-2025/discussion/596679
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ7RUqwrtwRD2EJbgMRrccAHkwUQZgFe2fsROCR1WV5LA1naxL0pU2grjQpcWC2HU3chdGwIOUpeuoK/pub?output=csv"

def get_global_shortests():
    response = requests.get(CSV_URL)
    response.raise_for_status()
    df = pd.read_csv(StringIO(response.text))

    task_start_idx = df.index[df.iloc[:, 0] == "TASK"][0] + 1
    task_df = df.iloc[task_start_idx:].reset_index(drop=True)
    task_df.rename(columns={task_df.columns[0]: "TASK"}, inplace=True)

    for col in task_df.columns[1:]:
        task_df[col] = pd.to_numeric(task_df[col], errors="coerce")

    top3_bytes = task_df.set_index("TASK").apply(
        lambda row: [int(size) for size in row.nsmallest(3).dropna()], axis=1
    )
    res = {'task' + task: sizes for task, sizes in top3_bytes.items() if sizes}
    return res
