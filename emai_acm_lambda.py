import boto3
import json
from datetime import datetime, timezone

# Initialize SNS client
sns_client = boto3.client('sns')

# SNS Topic ARN (Replace with your actual SNS topic ARN)
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:443841623847:ACM-Certificate-Expiry'

# Thresholds in days
THRESHOLDS = [90, 60, 30]

def publish_to_sns(subject, message):
    """
    Publishes the message to an SNS topic.
    """
    response = sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=subject,
        Message=message
    )
    print(f"Message published successfully. Response: {response}")

def lambda_handler(event, context):
    try:
        print(f"Received Event: {event}")

        # Parse invokingEvent JSON string into a dictionary
        invoking_event = json.loads(event['invokingEvent'])

        # Extract configuration item details
        configuration_item = invoking_event.get('configurationItem', {})
        configuration = configuration_item.get('configuration', {})

        # Extract required values
        account_id = configuration_item.get('awsAccountId', 'N/A')
        region = configuration_item.get('awsRegion', 'N/A')
        cert_arn = configuration.get('certificateArn', 'N/A')
        cert_domain = configuration.get('domainName', 'N/A')
        expiry_date_str = configuration.get('notAfter', None)

        if expiry_date_str:
            try:
                expiry_date = datetime.strptime(expiry_date_str, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)
            except ValueError:
                expiry_date = datetime.strptime(expiry_date_str, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)

            days_to_expiry = (expiry_date - datetime.now(timezone.utc)).days
        else:
            expiry_date = "Unknown"
            days_to_expiry = None

        print(f"Certificate Expiry Date: {expiry_date}, Days to Expiry: {days_to_expiry}")

        # Check if notification is needed
        if days_to_expiry and days_to_expiry in THRESHOLDS:
            message = f"""
                Dear APS Operations,

                The following ACM certificate is expiring soon:

                Account: {account_id}
                Region: {region}
                Certificate ARN: {cert_arn}
                Certificate Domain: {cert_domain}
                Expiry Date: {expiry_date}
                Remaining Days: {days_to_expiry}

                Please take appropriate action to renew or replace the certificate.

                Best regards,
                AWS Lambda Notification
            """

            subject = f"ACM Certificate Expiry Notification - {cert_domain} ({days_to_expiry} days left)"
            publish_to_sns(subject, message)

        return {"statusCode": 200, "body": "Notification processed successfully."}

    except Exception as e:
        print(f"Error: {str(e)}")
        return {"statusCode": 500, "body": f"Error: {str(e)}"}
