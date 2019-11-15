import logging
import json
from sym_api_client_python.processors.message_formatter import MessageFormatter
from sym_api_client_python.processors.sym_message_parser import SymMessageParser

from messages.messages import Messages

class RoomProcessor:
    def __init__(self, bot_client):
        self.bot_client = bot_client
        self.bot_id = self.bot_client.bot_id
        self.messages = Messages(self.bot_id)
        self.sym_message_parser = SymMessageParser()

    def process(self, msg):
        print(msg)
        logging.debug('im_processor/process_im_message()')
        logging.debug(json.dumps(msg, indent=4))

        user_id = msg['user']['userId']
        mentioned_users = self.sym_message_parser.get_mention_ids(msg)

        self.start_message = dict(message = """<messageML>
                                                <p>Choose Your Demo:</p>
                                                <br /> <br />
                                                  <form id='choose-bot'>
                                                    <div style='padding-top:1px;'><button type="action" name="kyc">KYC</button>
                                                    <button type="action" name="trade-structure">Trade Structure</button>
                                                    <button type="action" name="whitesand">WhiteSand</button></div>
                                                  </form>
                                                </messageML>
                    """)

        if mentioned_users:
            if mentioned_users[0] == self.bot_id and commands[0] == 'start':
                self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], self.start_message)

        else:
            self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], self.start_message)