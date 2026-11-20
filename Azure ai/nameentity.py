from openai import AzureOpenAI

deployment_name = "gpt-5-mini"
# Use the alternative standard Azure OpenAI resource endpoint and key from cell qh-BHZ7lOvyX
endpoint_clean = "https://24691a32j1-5906-resource.services.ai.azure.com/"
api_key_clean = "9c0p2SccRQiuNCS5r9fciRyxOrPN4mE1ZzRtsqA5pBkCQMTxB2h3JQQJ99CKACF24PCXJ3w3AAAAACOGjgmy"

client = AzureOpenAI(
    azure_endpoint=endpoint_clean,
    api_key=api_key_clean,
    api_version="2024-08-01-preview"
)

response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "user", "content": "You are a named entity recognition assistant. Extract all person names, organization names, and locations from the user's text, and return them in JSON format with keys 'persons', 'organizations', 'locations'."},
        {"role":"system","content":"Satya Nadella, CEO of Microsoft, announced a new partnership with the University of Washington in Seattle."}
    ]
)

print(f"answer: {response.choices[0].message.content}")