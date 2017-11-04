import os
from slackclient import SlackClient


class slackbot:

    def __init__(self, token=-1):
        if token == -1:
            slack_token = os.environ["SLACK_TOKEN_TRAINING"]
        else:
            slack_token = token
        self.sc = SlackClient(slack_token)

    def sendMessage(self, channel, text):
        self.sc.api_call("chat.postMessage", channel=channel, text=text)
