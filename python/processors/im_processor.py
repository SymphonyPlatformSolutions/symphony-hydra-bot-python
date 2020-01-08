import logging
import json
from sym_api_client_python.processors.message_formatter import MessageFormatter
from sym_api_client_python.processors.sym_message_parser import SymMessageParser
from listeners.render_form.render_form import render_form
import time

from messages.messages import Messages

class IMProcessor:
    def __init__(self, bot_client):
        self.bot_client = bot_client
        self.bot_id = self.bot_client.bot_id
        self.messages = Messages(self.bot_id)
        self.sym_message_parser = SymMessageParser()
        self.onboard_help_message = dict(message = """<messageML>
                                    <h3>Hi! Use hydraBot to assist with all your onboarding needs! You can try:</h3>
                                        <ul>
                                        <li><mention uid="{0}"/> help onboard</li>
                                        <li><mention uid="{0}"/> get entity</li>
                                        <li><mention uid="{0}"/> get documentation</li>
                                        <li><mention uid="{0}"/> clear</li>
                                        <li><mention uid="{0}"/> finish</li>
                                        </ul>
                                </messageML>
                    """.format(self.bot_id))

        self.trade_help_message = dict(message = """<messageML>
                                    <h3>Hi! Use hydraBot to assist with all your trading needs! You can try:</h3>
                                        <ul>
                                        <li><mention uid="{0}"/> help trade</li>
                                        <li><mention uid="{0}"/> find the yield</li>
                                        <li><mention uid="{0}"/> buy</li>
                                        <li><mention uid="{0}"/> finish</li>
                                        </ul>
                                </messageML>
                    """.format(self.bot_id))

        self.help_resolve_message = dict(message = """<messageML>
                                    <h3>Hi! Use hydraBot to keep you up to date on trade status! You can try:</h3>
                                        <ul>
                                        <li><mention uid="{0}"/> help resolve</li>
                                        <li><mention uid="{0}"/> get fx</li>
                                        <li><mention uid="{0}"/> get unmatched fx [currency]</li>
                                        <li><mention uid="{0}"/> finish</li>
                                        </ul>
                                </messageML>
                    """.format(self.bot_id))

        self.help_message = dict(message = """<messageML>
                                        <ul>
                                        <li><mention uid="{0}"/> help onboard</li>
                                        <li><mention uid="{0}"/> help trade</li>
                                        <li><mention uid="{0}"/> help resolve</li>
                                        <li><mention uid="{0}"/> finish</li>
                                        </ul>
                                </messageML>
                    """.format(self.bot_id))

    def process(self, msg):
        logging.debug('im_processor/process_im_message()')
        logging.debug(json.dumps(msg, indent=4))

        commands = self.sym_message_parser.get_text(msg)
        user_id = msg['user']['userId']
        mentioned_users = self.sym_message_parser.get_mention_ids(msg)

        if mentioned_users:
            if len(commands) > 2:
                if mentioned_users[0] == self.bot_id and commands[1] == 'help' and commands[2] == 'trade':
                    self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], self.trade_help_message)

                elif mentioned_users[0] == self.bot_id and commands[1] == 'help' and commands[2] == 'onboard':
                    self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], self.onboard_help_message)

                elif mentioned_users[0] == self.bot_id and commands[1] == 'help' and commands[2] == 'resolve':
                    self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], self.help_resolve_message)

                elif mentioned_users[0] == self.bot_id and commands[1] == 'get' and commands[2] == 'entity':
                    self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], self.messages.entity_message)
                    self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], self.messages.data_message)

                elif mentioned_users[0] == self.bot_id and commands[1] == 'get' and commands[2] == 'documentation':
                    self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], self.messages.entity_message)
                    self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], self.messages.documentation_message)

                elif mentioned_users[0] == self.bot_id and commands[1] == 'get' and commands[2] == 'fx':
                    self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], self.messages.match_message)
                    self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], render_form('/data/symphony/listeners/render_form/html/fx.html'))

                elif mentioned_users[0] == self.bot_id and commands[1] == 'get' and commands[2] == 'unmatched':
                    self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], self.messages.match_message)
                    self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], render_form('/data/symphony/listeners/render_form/html/jpy_fx.html'))

                elif mentioned_users[0] == self.bot_id and commands[1] == 'find' and commands[2] == 'the' and commands[3] == 'yield':
                    self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], render_form('/data/symphony/listeners/render_form/html/yield.html'))

                elif mentioned_users[0] == self.bot_id and commands[1] == 'buy':
                    self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], render_form('/data/symphony/listeners/render_form/html/buy_identifier.html'))

                elif mentioned_users[0] == self.bot_id and commands[1] == 'help':
                    self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], self.help_message)

                else:
                    self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], self.messages.understand_message)
            else:

                if mentioned_users[0] == self.bot_id and commands[1] == 'thanks':
                    self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], self.messages.thanks_message)

                elif mentioned_users[0] == self.bot_id and commands[1] == 'clear':
                    self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], self.messages.spaces_message)

                elif mentioned_users[0] == self.bot_id and commands[1] == 'finish':
                    self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], self.messages.finish_message)

                elif mentioned_users[0] == self.bot_id and commands[1] == 'yield':
                    self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], render_form('/data/symphony/listeners/render_form/html/yield.html'))

                elif mentioned_users[0] == self.bot_id and commands[1] == 'buy':
                    self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], render_form('/data/symphony/listeners/render_form/html/buy_identifier.html'))

                else:
                    self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], self.help_message)

        else:
            self.bot_client.get_message_client().send_msg(msg['stream']['streamId'], self.help_message)
