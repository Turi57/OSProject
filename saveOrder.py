import boto3

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
        QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team3'
    )
    
    if response == None:
        return None
    
    for order in response["Messages"]:
        listOrders.append(order["Body"])
    
    return listOrders
