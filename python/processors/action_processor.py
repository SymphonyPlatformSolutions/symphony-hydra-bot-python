import logging
import json
from sym_api_client_python.processors.message_formatter import MessageFormatter
from sym_api_client_python.processors.sym_elements_parser import SymElementsParser
from listeners.render_form.render_form import render_form
from messages.messages import Messages

class ActionProcessor:

    def __init__(self, bot_client):
        self.bot_client = bot_client
        self.bot_id = self.bot_client.bot_id
        self.messages = Messages(self.bot_id)

    def process_im_action(self, action):
        logging.debug('action_processor/im_process')
        logging.debug(json.dumps(action, indent=4))

        if SymElementsParser().get_form_values(action)['action'].startswith('data'):
            company_name = SymElementsParser().get_form_values(action)['action'].split(' ')
            self.data_message = MessageFormatter().format_message('Found your client company [{0}].  Now provide an entify identifier like [LEI, Client Identifier, or Exact Name Match]'.format(company_name))
            self.bot_client.get_message_client().send_msg(SymElementsParser().get_stream_id(action), self.data_message)
            self.bot_client.get_message_client().send_msg(SymElementsParser().get_stream_id(action), render_form('./listeners/render_form/html/data_identifier.html'))

        if SymElementsParser().get_form_values(action)['action'].startswith('docs'):
            print('in docs message')
            company_name = SymElementsParser().get_form_values(action)['action'].split(' ')
            self.docs_message = MessageFormatter().format_message('Found your client company [{0}].  Now provide an entify identifier like [LEI, Client Identifier, or Exact Name Match]'.format(company_name))
            self.bot_client.get_message_client().send_msg(SymElementsParser().get_stream_id(action), self.docs_message)
            self.bot_client.get_message_client().send_msg(SymElementsParser().get_stream_id(action), render_form('./listeners/render_form/html/doc_identifier.html'))

        elif SymElementsParser().get_form_values(action)['action'] == 'identifier-data':
            form_contents = SymElementsParser().get_form_values(action)
            self.bot_client.get_message_client().send_msg(SymElementsParser().get_stream_id(action), render_form('./listeners/render_form/html/data_table.html'))

        elif SymElementsParser().get_form_values(action)['action'] == 'identifier-doc':
            form_contents = SymElementsParser().get_form_values(action)
            self.bot_client.get_message_client().send_msg(SymElementsParser().get_stream_id(action), self.messages.table_message)
            self.bot_client.get_message_client().send_msg(SymElementsParser().get_stream_id(action), render_form('./listeners/render_form/html/doc_table.html'))

        elif SymElementsParser().get_form_values(action)['action'] == 'clear':
            self.bot_client.get_message_client().send_msg(SymElementsParser().get_stream_id(action), self.messages.clear_message)

        elif SymElementsParser().get_form_values(action)['action'] == 'finish':
            self.bot_client.get_message_client().send_msg(SymElementsParser().get_stream_id(action), self.messages.spaces_message)

        elif SymElementsParser().get_form_values(action)['action'].startswith('fix'):
            user_id = SymElementsParser().get_initiator_user_id(action)
            values = SymElementsParser().get_form_values(action)['action'].split(' ')
            room_name = values[1]
            message_number = int(values[2])
            print(message_number)

            room_obj = {
                "name" : str(room_name),
                "description" : str(room_name)
            }
            stream = self.bot_client.get_stream_client().create_room(room_obj)['roomSystemInfo']['id']
            self.bot_client.get_stream_client().add_member_to_room(stream, user_id)
            self.bot_client.get_message_client().send_msg(stream, self.messages.fx_messages[message_number])
            self.bot_client.get_message_client().send_msg(SymElementsParser().get_stream_id(action), render_form('./listeners/render_form/html/fx.html'))


        elif SymElementsParser().get_form_values(action)['action'].startswith('jpy'):
            user_id = SymElementsParser().get_initiator_user_id(action)
            values = SymElementsParser().get_form_values(action)['action'].split(' ')
            room_name = values[1]
            message_number = int(values[2])
            print(message_number)

            room_obj = {
                "name" : str(room_name),
                "description" : str(room_name)
            }
            stream = self.bot_client.get_stream_client().create_room(room_obj)['roomSystemInfo']['id']
            self.bot_client.get_stream_client().add_member_to_room(stream, user_id)
            self.bot_client.get_message_client().send_msg(stream, self.messages.jpy_fx_messages[message_number])
            self.bot_client.get_message_client().send_msg(SymElementsParser().get_stream_id(action), render_form('./listeners/render_form/html/jpy_fx.html'))


    def process_room_action(self, action):
        logging.debug('action_processor/room_process')
        logging.debug(json.dumps(action, indent=4))

        if SymElementsParser().get_form_values(action)['action'] == 'kyc':
            user_id = SymElementsParser().get_initiator_user_id(action)
            kyc_im = self.bot_client.get_stream_client().create_im([user_id])
            self.kyc_message = dict(message = """<messageML>
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
            self.bot_client.get_message_client().send_msg(kyc_im['id'], self.kyc_message)

        if SymElementsParser().get_form_values(action)['action'] == 'trade-structure':
            user_id = SymElementsParser().get_initiator_user_id(action)
            kyc_im = self.bot_client.get_stream_client().create_im([user_id])
            self.trade_message = dict(message = """<messageML>
                                        <h3>Hi! Use hydraBot to assist with all your trading needs! You can try:</h3>
                                            <ul>
                                            <li><mention uid="{0}"/> help trade</li>
                                            <li><mention uid="{0}"/> find the yield</li>
                                            <li><mention uid="{0}"/> buy</li>
                                            <li><mention uid="{0}"/> finish</li>
                                            </ul>
                                    </messageML>
                        """.format(self.bot_id))
            self.bot_client.get_message_client().send_msg(kyc_im['id'], self.trade_message)

        if SymElementsParser().get_form_values(action)['action'] == 'whitesand':
            user_id = SymElementsParser().get_initiator_user_id(action)
            kyc_im = self.bot_client.get_stream_client().create_im([user_id])
            self.whitesand_message = dict(message = """<messageML>
                                        <h3>Hi! Use hydraBot to keep you up to date on trade status! You can try:</h3>
                                            <ul>
                                            <li><mention uid="{0}"/> help resolve</li>
                                            <li><mention uid="{0}"/> get fx</li>
                                            <li><mention uid="{0}"/> get unmatched fx [currency]</li>
                                            <li><mention uid="{0}"/> finish</li>
                                            </ul>
                                    </messageML>
                        """.format(self.bot_id))
            self.bot_client.get_message_client().send_msg(kyc_im['id'], self.whitesand_message)
