from sym_api_client_python.processors.message_formatter import MessageFormatter
from listeners.render_form.render_form import render_form

class Messages:
    def __init__(self, bot_id):

        self.clear_message = dict(message = """<messageML>
                                        <p>Begin a new request</p>
                                      </messageML>""")

        self.spaces_message = dict(message = """<messageML>
                                        <br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
                                      </messageML>""")


        self.data_message = dict(message = """<messageML>
                                          <form id="form_id">
                                            <div style='padding-top:1px;padding-left:5px;'>
                                                <button name="data MK-Capitol" type="action">MK Captiol</button>
                                                <button name="data Hudson-Exchange" type="action">Hudson Exchange</button>
                                                <button name="data Reed Trading Co" type="action">Reed Trading Co.</button>
                                            </div>
                                          </form>
                                       </messageML>""".format(bot_id))

        self.finish_message = dict(message = """<messageML>
                                          <form id="form_id">
                                          <br />
                                            <div style='padding-top:1px;padding-left:5px;'>
                                                <button name="finish" type="action">FINISH</button>
                                            </div>
                                          </form>
                                       </messageML>""".format(bot_id))

        self.documentation_message = dict(message = """<messageML>
                                          <form id="form_id">
                                            <div style='padding-top:1px;padding-left:5px;'>
                                                <button name="docs MK-Capitol" type="action">MK Captiol</button>
                                                <button name="docs Hudson-Exchange" type="action">Hudson Exchange</button>
                                                <button name="docs Reed Trading Co" type="action">Reed Trading Co.</button>
                                            </div>
                                          </form>
                                       </messageML>""".format(bot_id))

        self.entity_message = MessageFormatter().format_message('Please select a client entity name to start')
        self.bye_message = MessageFormatter().format_message('Thanks for using!')
        self.thanks_message = MessageFormatter().format_message('No Problem!')
        self.buy_message = MessageFormatter().format_message('Building order for you')
        self.match_message = MessageFormatter().format_message('Here is FX Trade Match Search Results')
        self.understand_message = MessageFormatter().format_message('Sorry I did not quite catch that, one more time please?')
        self.table_message = dict(message = """<messageML>
          <table>
              <tbody>
                <tr>
                  <td>W-88EN-E</td>
                </tr>
                <tr>
                  <td>Audited Financial Statements</td>
                </tr>
                <tr>
                  <td>Assests Under Management (AUN)</td>
                </tr>
                <tr>
                  <td>Sub-Legal Classification</td>
                </tr>
                <tr>
                  <td>Articles of Organization</td>
                </tr>
                <tr>
                  <td>LLC Agreement</td>
                </tr>
                <tr>
                  <td>Investment Management Agreement</td>
                </tr>
                <tr>
                  <td>Offering Memorandum/Prospectus/Offering Circular</td>
                </tr>
                <tr>
                  <td>Account Opening Form</td>
                </tr>
              </tbody>
          </table>
        </messageML>""".format(bot_id))

        self.fx_messages = {
                            1 : render_form('python/listeners/render_form/html/fx/1.html'),
                            2 : render_form('python/listeners/render_form/html/fx/2.html'),
                            3 : render_form('python/listeners/render_form/html/fx/3.html'),
                            4 : render_form('python/listeners/render_form/html/fx/4.html'),
                            5 : render_form('python/listeners/render_form/html/fx/5.html'),
                            6 : render_form('python/listeners/render_form/html/fx/6.html')
                        }

        self.jpy_fx_messages = {
                            1 : render_form('python/listeners/render_form/html/jpy/jpy_1.html'),
                            2 : render_form('python/listeners/render_form/html/jpy/jpy_2.html'),
                            3 : render_form('python/listeners/render_form/html/jpy/jpy_3.html'),
                            4 : render_form('python/listeners/render_form/html/jpy/jpy_4.html'),
                            5 : render_form('python/listeners/render_form/html/jpy/jpy_5.html'),
                            6 : render_form('python/listeners/render_form/html/jpy/jpy_6.html'),
                            7 : render_form('python/listeners/render_form/html/jpy/jpy_7.html'),
                            8 : render_form('python/listeners/render_form/html/jpy/jpy_8.html'),
                            9 : render_form('python/listeners/render_form/html/jpy/jpy_9.html'),
                            10 : render_form('python/listeners/render_form/html/jpy/jpy_10.html')
                        }
