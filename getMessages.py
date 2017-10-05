import boto3

def getMessages():
    access_key = 'AKIAIYNWJ4DC5WPKXSYA'
    secret_access_key = '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'
    sqs = boto3.client('sqs',aws_access_key_id=access_key,aws_secret_access_key=secret_access_key,region_name='us-east-1')
    response = sqs.receive_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team3'
    )

    for message in response["Messages"]:
        print(message['Body'])

getMessages()
