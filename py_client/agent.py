import requests

prompts = {
    1: """We are planning an Agentic AI project that builds word documents based on plain human prompts. The app will take user prompt, this prompt will be sent to LLMs that will generate the task (for subsequent LLM) and finally create the word doc. Please help us create a word doc for this.""",

    2: """Generate meeting minutes for a weekly software development team meeting discussing sprint progress, completed tasks, blockers, action items, and deadlines.""",

    3: """We are planning to build a Smart Inventory Management System for retail stores. Create a professional project proposal that includes an executive summary, project objectives, key features, technology stack, implementation timeline, expected benefits, and conclusion.""",

    4: """Prepare a research report on the impact of Artificial Intelligence in healthcare. Include an introduction, literature review, major applications, benefits, challenges, future trends, and references.""",

    5: """Please help me summarise my uploaded file"""
}


data = dict(
    request = prompts[5]
)

response = requests.post("http://127.0.0.1:8000/agent/", json = data)
if response.status_code == 200:
    print(response.json())
else:
    print(response.text)