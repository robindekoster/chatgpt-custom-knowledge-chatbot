import openai


def main():
    messages = [
        {"role": "system", "content": "You’re a kind helpful assistant, only respond with knowledge knowledge you "
                                      "know for sure, dont hallucinate information."},
        {"role": "user", "content": "Your only knowledge is about the lifespan of a dog, it depends on various "
                                    "factors like breed, size, and overall health. On average, a small dog can live "
                                    "for up to 15 years, while a medium-sized dog can live for around 12 years, "
                                    "and a large dog can live up to 8 years. However, some dogs have been known to "
                                    "live to be as old as 20 years or more with proper care and regular visits to the "
                                    "veterinarian."}  # Replace with custom knowledge base.
    ]

    while True:
        content = input("User: ")
        messages.append({"role": "user", "content": content})

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        chat_response = completion.choices[0].message.content
        print(f'ChatGPT: {chat_response}')
        messages.append({"role": "assistant", "content": chat_response})


if __name__ == '__main__':
    main()
