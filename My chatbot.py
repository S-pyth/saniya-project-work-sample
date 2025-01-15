import openai
openai.api_key="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"
def chatbot(prompt):
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        message=[{"role":"user","content":prompt}]
    )
    return response.Choices[0].message.content.strip()
def main():
    while True:
        prompt=input("prompt:")
        if prompt.lower()=="q":
            break
        print("Response:",chatbot(prompt))
main()       
