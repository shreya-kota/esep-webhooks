import os
import json
import requests

def lambda_handler(event, context):
    github_event = json.loads(event['body'])
    issue_url = github_event['issue']['html_url']
    payload = {"text": f"Issue Created: {issue_url}"}
    slack_webhook_url = os.environ.get('SLACK_URL')
    response = requests.post(slack_webhook_url, json=payload)
    if response.status_code == 200:
        return {
            'statusCode': 200,
            'body': json.dumps('Message sent to Slack successfully!')
        }
    else:
        return {
            'statusCode': response.status_code,
            'body': json.dumps('Failed to send message to Slack!')
        }
