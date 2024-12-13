from flask import Flask, request, jsonify
# from openai import OpenAI
from dotenv import load_dotenv
from openai import OpenAI
import os

app = Flask(__name__)

# Load the .env file
load_dotenv()

# Access the environment variable
api_key = os.getenv('openapi_key')

client = OpenAI(
    api_key=api_key,
    # organization='org-iHaqOC7mm7E39xcpJgWplPQC',
    # project='proj_wKBLQILIaPhUr4U7vnwIU9dE',
)

@app.get("/healthcheck")
def healthcheck():
    return "healthy"

@app.post("/component")
def generate_component():
    data = request.get_json()
    message = data['message']
    completion = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {
                "role": "system",
                "content": "You are a typescript coding assistant that generates react components. You only respond with the code of the function component. You don't respond with anything else that is not the function component such as an explanataion of the code. Do not include import statements. Do not include markdown."
            },
            {
                "role": "system",
                "content": "Do not include import statements."
            },
            {
                "role": "system",
                "content": "Do not include markdown."
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )
    result = completion.choices[0].message.content
    print(result)
    # return result
    return {"component": result}





if __name__ == "__main__":
    app.run(debug=True)
