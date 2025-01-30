import boto3
from datetime import datetime, timedelta, timezone

# Initialize clients
acm_client = boto3.client('acm')
sns_client = boto3.client('sns')

# SNS Topic ARN
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:443841623847:ACM-Certificate-Expiry'  # Replace with your SNS topic ARN

# Thresholds in days
THRESHOLDS = [90, 60, 30]

def publish_to_sns(subject, message):
    sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=subject,
        Message=message
    )

def handle_config_event(event):
    for record in event.get('invokingEvent', {}).get('configurationItemDiff', {}).get('changedProperties', []):
        if 'NotAfter' in record:
            expiry_date = datetime.strptime(record['NotAfter'], '%Y-%m-%dT%H:%M:%SZ')
            days_to_expiry = (expiry_date - datetime.utcnow()).days
            if days_to_expiry in THRESHOLDS:
                # Example alert for expired certificates
                publish_to_sns(
                    subject=f"ACM Certificate Expiry Alert",
                    message=f"Certificate expiring in {days_to_expiry} days!"
                )

def lambda_handler(event, context):
    try:
        # handle_config_event(event)
        print(f"Event : {event}")
        print(event['invokingEvent']['configurationItem']['configuration']['awsAccountId'])
        account_id = event['invokingEvent']['configurationItem']['configuration']['awsAccountId']
        region = event['invokingEvent']['configurationItem']['configuration']['awsRegion']
        cert_arn = event['invokingEvent']['configurationItem']['configuration']['certificateArn']
        cert_domain = event['invokingEvent']['configurationItem']['configuration']['domainName']
        expiry_date = datetime.now(timezone.utc) + timedelta(days=30)
        days_to_expiry = (expiry_date - datetime.now(timezone.utc)).days

        message = f"""
                Dear APS Operations,

                The following ACM certificate is expiring soon:

                Account: {account_id}
                Region: {region}
                Certificate ARN: {cert_arn}
                Certificate Domain: {cert_domain}
                Expiry Date: {expiry_date}
                Remaining Days: {days_to_expiry}
                Resources Attached: 

                Please take appropriate action to renew or replace the certificate.

                Best regards,
                AWS Lambda Notification
                """
        print(message)
        response = sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="ACM Certificate Expiry Notification for {cert_domain}",
            Message=message
        )

        print(f"Message published successfully. Response: {response}")
        
        return {"statusCode": 200, "body": "Notifications sent successfully."}
    except Exception as e:
        return {"statusCode": 500, "body": f"Error: {str(e)}"}
