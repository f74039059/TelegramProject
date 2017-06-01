import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

API_TOKEN = '393540263:AAHYuCuSKAQ6INwRkergnNsQa-ciah5C7A8'
WEBHOOK_URL = 'https://20ca36b0.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
                     states=[
                             'user',
                             'state1',
                             'state2',
                             'state3',
                             'state4',
                             'state5',
                             'state6',
                             'state7',
                             'state8'
                             ],
                     transitions=[
                                  {
                                  'trigger': 'advance',
                                  'source': 'user',
                                  'dest': 'state1',
                                  'conditions': 'is_going_to_state1'
                                  },
                                  {
                                  'trigger': 'advance',
                                  'source': 'state1',
                                  'dest': 'state3',
                                  'conditions': 'is_going_to_state1to3'
                                  },
                                  {
                                  'trigger': 'advance',
                                  'source': 'state3',
                                  'dest': 'state1',
                                  'conditions': 'is_going_to_state3to1'
                                  },
                                  {
                                  'trigger': 'advance',
                                  'source': 'state3',
                                  'dest': 'state4',
                                  'conditions': 'is_going_to_state3to4'
                                  },
                                  
                                  {
                                  'trigger': 'advance',
                                  'source': 'user',
                                  'dest': 'state2',
                                  'conditions': 'is_going_to_state2'
                                  },
                                  {
                                  'trigger': 'advance',
                                  'source': 'user',
                                  'dest': 'state6',
                                  'conditions': 'is_going_to_state6'
                                  },
                                  {
                                  'trigger': 'advance',
                                  'source': 'state6',
                                  'dest': 'state7',
                                  'conditions': 'is_going_to_state6to7'
                                  },
                                  
                                  {
                                  'trigger': 'advance',
                                  'source': 'state6',
                                  'dest': 'state7',
                                  'conditions': 'is_going_to_state6to7'
                                  },
                                  {
                                  'trigger': 'advance',
                                  'source': 'state7',
                                  'dest': 'state8',
                                  'conditions': 'is_going_to_state7to8'
                                  },
                                  {
                                  'trigger': 'advance',
                                  'source': 'state4',
                                  'dest': 'state5',
                                  'conditions': 'is_going_to_state4to5'
                                  },
                                  {
                                  'trigger': 'go_back',
                                  'source': [
                                             'state5',
                                             'state2',
                                             'state8'
                                             ],
                                  'dest': 'user'
                                  }
                                  ],
                     initial='user',
                     auto_transitions=False,
                     show_conditions=True,
                     )



machine.show_graph()
def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()




