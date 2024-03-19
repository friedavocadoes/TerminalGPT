import openai

def apier():
    api = input("Input your API Key: ")
    api.rstrip('\n')
    f2 = open("API.txt", 'w')
    f2.write(api)
    f2.close()

f = open("API.txt", 'r+')

api = f.read()
while api == "":
     apier()
     api = f.read()

f.close()

openai.api_key = api

def get_bot_response(user_input):
    try:
        response = openai.chat.completions.create(
            model="davinci-002",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return "Error: {}".format(e)

def main():
    print("Welcome to the OpenAI Chatbot! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        bot_response = get_bot_response(user_input)
        print("Bot:", bot_response)

if __name__ == "__main__":
    main()
