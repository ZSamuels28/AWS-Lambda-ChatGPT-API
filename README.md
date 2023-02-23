# AWS Lambda + API Gateway for ChatGPT
#### Note: this project uses the revChatGPT library found at https://github.com/acheong08/ChatGPT. Thanks to that team for making this possible.

## Description
This project allows you to utilize your ChatGPT account with AWS Lambda + AWS API Gateway to create your own serverless ChatGPT API.

## Setup and Config
### Creating the Lambda Function
1. If you don't already have one, you will need to create an AWS account
2. Once logged into AWS, go to AWS Lambda and create a new Lambda Function from scratch
3. Copy and paste the code in the lambda_function.py to your AWS Lambda function
4. Deploy this code and save
5. Go to Configuration -> General Configuration. You will likely want to edit the Timeout (I set it at 1 minute) as if you don't have a paid ChatGPT account, the responses can take some time
6. Go to Configuration -> Environment variables and create 2 environment variables: 

| Variable Name  | Value |
| ------------- | ------------- |
| USERNAME  | Enter your ChatGPT email  |
| PASSWORD  | Enter your ChatGPT password  |

### Creating the API Gateway
1. In the main AWS Lambda function page for the function overview, click Add trigger
2. Select API Gateway as the trigger configuration
3. Create a new REST API and set the Security to your liking (for testing purposes I made mine open)
4. Once that is created you can click on the API Gateway and see the endpoint

### Uploading revChatGPT as a Lambda Layer
1. Since we need the revChatGPT library included to utilize the Lambda Function, we will need to create a Lambda Layer
2. See https://www.linkedin.com/pulse/add-external-python-libraries-aws-lambda-using-layers-gabe-olokun/ on creating a Lambda Layer utilizing AWS and when getting to the pip install section, make sure you `pip install revChatGPT -t .`

### Calling the API
1. Once all of the above is done, you should have a function that has revChatGPT as a layer and an API Gateway endpoint
2. Using your preferred method of calling the API send the following JSON body to the API endpoint you created above: 
```json
{
    "Question" : "Can you confirm this is working?"
}
```
3. You should receive a response generated from ChatGPT. If you receive an error, please take a look at CloudWatch or open an issue.
