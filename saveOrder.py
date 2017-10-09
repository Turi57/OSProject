import boto3

def saveOrder():

    f = open("orders.json", 'a')
    sqs = boto3.client('sqs')
    response = sqs.receive_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team3'
    )

    for order in response["Messages"]:
        f.write(order["Body"] + "\n")
        print(order)

saveOrder()
