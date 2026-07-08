from agent import agent

app = agent

prompts = {
    1: """We are planning an Agentic AI project that builds word documents based on plain human prompts. The app will take user prompt, this prompt will be sent to LLMs that will generate the task (for subsequent LLM) and finally create the word doc. Please help us create a word doc for this.""",

    2: """Generate meeting minutes for a weekly software development team meeting discussing sprint progress, completed tasks, blockers, action items, and deadlines.""",

    3: """We are planning to build a Smart Inventory Management System for retail stores. Create a professional project proposal that includes an executive summary, project objectives, key features, technology stack, implementation timeline, expected benefits, and conclusion.""",

    4: """Prepare a research report on the impact of Artificial Intelligence in healthcare. Include an introduction, literature review, major applications, benefits, challenges, future trends, and references."""
}

user_input = prompts[2]

try:
    app.invoke(dict(
        messages=[("user", user_input)]
    ))
    print("TODO generated!")
except Exception as err:
    print(f"[ERR]: {str(err)}")