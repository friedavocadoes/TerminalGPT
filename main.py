import openai


def get_bot_response(user_input):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo-1106",
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
