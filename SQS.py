import boto3
import json

def saveOrder():
    f = open("orders.json", 'a')
    sqs = boto3.client('sqs')
    response = sqs.receive_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team3'
    )
    
    # If the response is empty, close the file and return
    if response == None:
        f.close()
        return
    
    # Save json strings from response in orders.json and print them to system.out
    for order in response["Messages"]:
        f.write(order["Body"] + "\n")
        print(order)
    f.close()

def readSQS():
    listOrders = []
    sqs = boto3.client('sqs')
    response = sqs.receive_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team3',
        MaxNumberOfMessages=3
    )

    if response != None:
        for order in response["Messages"]:
            listOrders.append(json.loads(order["Body"]))

    return listOrders

def putSQS(message):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='cc406_team3')
    print(queue.url)

    response = queue.send_message(MessageBody=message)
