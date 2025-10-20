import os
from openai import OpenAI

key = "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"

messages = []
client = OpenAI(
    api_key = key,      #OpenAI client
)
def completion(message):
    global messages
    messages.append(
            {
                "role" : "user",
                "content" : message,
            }
        )
    chat_completion = client.chat.completions.create(
        model = "gpt-4o",
        messages = messages
        )
    
    #print(chat_completion)

    message = {
        "role" : "assistant",
        "content" : chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"Sofia : {message["content"]}\n")

if __name__ == "__main__":
    print("Sofia : Hi, I am Sofia, How may I help You :)")
    while True:
        user_question = input()
        completion(user_question)