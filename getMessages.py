import boto3

def getMessages():


    sqs = boto3.client('sqs')
    response = sqs.receive_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team3'
    )

    for message in response["Messages"]:
        print(message['Body'])

getMessages()
