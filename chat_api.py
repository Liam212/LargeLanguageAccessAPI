import openai
# import os

openai.api_type = "openai"
openai.api_key = "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"

def chat(messages, temperature=0.8, model='gpt-3.5-turbo', max_tokens=150, top_p=1, frequency_penalty=0, presence_penalty=0):
    chat_response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )

    print(chat_response)

    return chat_response['choices'][0]['message']['content'] # type: ignore

    