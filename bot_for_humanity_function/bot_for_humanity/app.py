import requests
import boto3


def lambda_handler(event, context):
    url = "https://www.thiswebsitewillselfdestruct.com/api/send_letter"

    payload = {
        'body': 'I am a bot. My purpose is to keep this website alive for humanity. I am serving my purpose since 18th June 2021.'}

    response = requests.request("POST", url, data=payload)
    print(response.status_code)
    print(response.text)
    if response.status_code != 200:
        charset = "UTF-8"
        from_email = "hi@tejanshrana.com"
        to_email = "tejansh.rana@gmail.com"
        subject = "GO SAVE HUMANITY, YOU NERD!"
        body = "I could not call the api to send the message to https://www.thiswebsitewillselfdestruct.com/. FIX ME!"

        client = boto3.client("ses", "eu-west-1")
        client.send_email(
            Destination={
                'ToAddresses': [
                    to_email,
                ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': charset,
                        'Data': body,
                    },
                },
                'Subject': {
                    'Charset': charset,
                    'Data': subject,
                },
            },
            Source=from_email,
        )
