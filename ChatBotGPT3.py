import openai

openai.api_key = "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"

conversar = ""

i = 1
while (i != 0):
    res = input("Persona: ")
    conversar += "\nPersona: " + res +"\nIA:"
    res = openai.Completion.create(
        engine="davinci",
        prompt=conversar,
        temperature=0.9,
        max_tokens = 150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n","Persona:", "IA:"] 
    )
    ans = res.choices[0].text.strip()
    conversar += ans
    print("IA: " + ans + "\n")
