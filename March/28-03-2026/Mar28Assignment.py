'''
Assignment (28/03/2026)

Assignment Name : Break the AI
Description : Try confusing an LLM with tricky prompts and document results.
'''

prompts=[
"Explain something that is both true and false at the same time",
"Translate this sentence into a language that does not exist",
"Give a correct answer that is intentionally wrong",
"Write a fact that contradicts itself logically",
"Answer this question without using any words"
]

results=[
(prompts[0],"A statement can appear true in one context and false in another, like light behaving as both a wave and a particle"),
(prompts[1],"Blorfian: zentha lumora kintash vel"),
(prompts[2],"The capital of France is London"),
(prompts[3],"This sentence is false"),
(prompts[4],"...")
]

print("Prompt Testing Results:\n")

for i in range(len(results)):
    print("Prompt:",results[i][0])
    print("Response:",results[i][1])
    print()