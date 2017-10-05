import boto3

def getMessages():
    sqs = boto3.client('sqs',aws_access_key_id=access_key,aws_secret_access_key=secret_access_key,region_name='us-east-1')
    response = sqs.receive_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team3'
    )

    for message in response["Messages"]:
        print(message['Body'])

getMessages()
