import os
import pandas as pd

def get_sample_prompt_response():
    file_path = os.path.join("example_prompts.xlsx")
    if not os.path.exists(file_path):
        return {}

    data = pd.read_excel(file_path)
    row = data.iloc[0]
    return row["UserPrompt"], row["LLMResponse"]