## Use this Lambda function to turn on an EC2 instance at 8am UTC every Monday
1. Create a Lambda function:
    a. Function name: turn-on-instance
    b. Runtime: Python 3.6
    c. Role: create a new role with basic Lambda permissions
2. Copy the code into Lambda's lambda_function.py
3. Create EventBridge rule:
    a. Rule name: turn-on-instance
    b. Description: turn on EC2 instance at 8am UTC every Monday
    c. Event Schedule: 0 8 ? * MON *
    d. Target: turn-on-instance (Lambda function)