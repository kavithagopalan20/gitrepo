from openai import OpenAI, APIError

client = OpenAI()

try:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input="Summarize this text: AI is transforming major industriws and it this si cool...."
    )
    print(response.output[0].content[0].text)
except APIError as e:
    print("OpenAI API error:", e)
