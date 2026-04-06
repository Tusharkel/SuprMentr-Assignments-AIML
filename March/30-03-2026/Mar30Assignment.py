'''
Assignment (30/03/2026)

Assignment Name : Prompt Engineer
Description : Write prompts for resume, business idea, study plan and compare weak vs strong prompts.
'''
tasks=["resume","business idea","study plan"]

weak_prompts=[
"make my resume",
"give me a business idea",
"help me study"
]

strong_prompts=[
"Create a professional resume for a final year computer science student with skills in python, machine learning and web development including projects and internships",
"Generate a scalable business idea in the AI domain with target users, revenue model and key features",
"Design a 4 week study plan for learning machine learning covering theory, coding practice and revision with daily schedule"
]

print("Prompt Comparison:\n")

for i in range(len(tasks)):
    print("Task:",tasks[i])
    print("Weak Prompt:",weak_prompts[i])
    print("Strong Prompt:",strong_prompts[i])
    print()