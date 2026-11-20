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
        {
            "role": "system",
            "content": "You are a text summarization assistant. Summarize the given text into 2-5 simple sentences. Include only the important information."
        },
        {
            "role": "user",
            "content": """
            Artificial Intelligence is a branch of computer science 
            that focuses on creating machines capable of performing 
            tasks that normally require human intelligence. AI is used 
            in healthcare, education, banking, agriculture, and transportation.
            Machine learning and deep learning are important technologies 
            used in AI applications.
            """
        }
    ]
)

print(f"answer: {response.choices[0].message.content}")