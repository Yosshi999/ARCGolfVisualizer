import pandas as pd
import requests
from io import StringIO

# https://www.kaggle.com/competitions/google-code-golf-2025/discussion/596679
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ7RUqwrtwRD2EJbgMRrccAHkwUQZgFe2fsROCR1WV5LA1naxL0pU2grjQpcWC2HU3chdGwIOUpeuoK/pub?output=csv"

def get_task_min_bytes():
    response = requests.get(CSV_URL)
    response.raise_for_status()
    df = pd.read_csv(StringIO(response.text))

    task_start_idx = df.index[df.iloc[:, 0] == "TASK"][0] + 1
    task_df = df.iloc[task_start_idx:].reset_index(drop=True)
    task_df.rename(columns={task_df.columns[0]: "TASK"}, inplace=True)

    for col in task_df.columns[1:]:
        task_df[col] = pd.to_numeric(task_df[col], errors="coerce")

    min_bytes = task_df.set_index("TASK").min(axis=1, skipna=True)
    res = {'task' + task: int(size) for task, size in min_bytes.items() if size is not None}
    return res
