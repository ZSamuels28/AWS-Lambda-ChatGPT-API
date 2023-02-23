import json
import os
from revChatGPT.V1 import Chatbot

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body'))
        question = body.get('Question')
        if not question:
            raise ValueError("No question provided")

        chatbot = Chatbot(
            config={"email": os.getenv('USERNAME'), "password": os.getenv('PASSWORD')}
        )

        response = ""

        for data in chatbot.ask(question):
            response = data["message"]

        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }
