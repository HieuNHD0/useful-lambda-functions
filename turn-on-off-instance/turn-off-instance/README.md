## Use this Lambda function to turn off an EC2 instance at 5pm UTC every Friday
1. Create a Lambda function:
    a. Function name: turn-off-instance
    b. Runtime: Python 3.6
    c. Role: create a new role with basic Lambda permissions
2. Copy the code into Lambda's lambda_function.py
3. Create EventBridge rule:
    a. Rule name: turn-off-instance
    b. Description: turn off EC2 instance at 5pm UTC every Friday
    c. Event Schedule: 0 17 ? * FRI *
    d. Target: turn-off-instance (Lambda function)