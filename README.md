# Full-Stack Serverless AWS Template

This project serves as a template for fullstack serverless web applications configured for AWS deployment using CloudFormation.

## Included AWS Services 

This template integrates with the following AWS services:

* **AWS Lambda**: To handle backend business logic.
* **DynamoDB**: A managed NoSQL database service for storage.
* **API Gateway**: To handle HTTP requests and responses.

## Preconfigured Permissions

Preconfigured permissions are set up for the Lambda functions to access DynamoDB. Basic actions such as GET, PUT, and DELETE have been defined.

## Directory Structure

Here's the structure of the project:
```
fullstack-serverless (root project folder)
├── frontend (folder for frontend configuration)
│   ├── jss
│   ├── css
│   └── html
├── lambda-functions (folder for Lambda functions)
│   ├── deleteFunction.py
│   ├── getFunction.py
│   └── putFunction.py
├── event_delete.json (for testing Lambda)
├── event_get.json 
├── event_put.json 
├── README.md (this file)
├── samconfig.toml (config for SAM deployment)
└── template.yaml (cloudformation template)
```

## Resources Created via CloudFormation

The `template.yaml` file defines the resources to be created using AWS CloudFormation. These resources include:

* **IAM Role** for Lambda functions that allows access to DynamoDB.
* **Lambda functions** for GET, PUT, and DELETE operations.
* **DynamoDB table** with the name "cloud9_table".
* **API Gateway** endpoint URL for the Prod stage.

To understand more about these resources, refer to the `template.yaml` file in the root project folder.

## Getting Started

This template is designed to help you quickly set up and launch a full stack serverless application. Below are the steps you can follow to use this template.

1. **Clone the Repository**

Start by cloning this repository to your local machine.

```bash
git clone https://github.com/<your-username>/fullstack-serverless-AWS.git
```
2. **Install the AWS SAM CLI**

If you have not already done so, install the AWS SAM CLI (https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html). This tool is necessary to build and deploy your application.

3. **Build the Application**

Navigate to the project directory and use SAM to build the application 

```bash
cd fullstack-serverless-AWS
sam build
```
4. **Deploy the Application**

Deploy your application using SAM. This will create the neccesary resources defined in your `template.yaml` file.

```bash
sam deploy --guided
```
Follow the prompts in the deploy process to set the stack name, AWS Region and other parameters.

5. **Test the Application**

Once deployment is successful, SAM will output the API Gateway URL which you can use to test your API. Test it by sending requests to the endpoints with a tool like curl or Postman.

6. **Customize as Needed**

Now that your serverless application is up and running, you can begin customizing the template to fit your specific needs. You can add new Lambda functions, modify the existing ones, or extend the DynamoDB table as needed.






















