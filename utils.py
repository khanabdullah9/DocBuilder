import os
import pandas as pd

def get_sample_prompt_response():
    file_path = os.path.join("example_prompts.xlsx")
    if not os.path.exists(file_path):
        return {}

    data = pd.read_excel(file_path)
    row = data.iloc[0]
    return row["UserPrompt"], row["LLMResponse"]

def read_todo():
    file_path = os.path.join("task","TODO.md")
    if not os.path.exists(file_path):
        return ""

    with open(file_path, "r") as f:
        content = f.read()

    return content

def read_document():
    file_path = os.path.join("generated","demo.docx")
    if not os.path.exists(file_path):
        return ""

    with open(file_path, "r") as f:
        content = f.read()

    return content