import openai

openai.api_key = "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"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response.choices[0].text.strip()