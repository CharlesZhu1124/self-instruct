import openai

openai.api_type = "azure"
openai.api_base = "https://dsa-gpt-demo.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "f144be73403f41da8c7a453342f48cd4"

response = openai.Completion.create(
    engine='text-davinci-003',
    prompt='Once upon a time',
    max_tokens=100
)

generated_text = response.choices[0].text.strip()
print(generated_text)