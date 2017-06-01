from transitions.extensions import GraphMachine
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import os, sys, inspect
import logging
import telegram.ext
from telegram.ext import Updater, CommandHandler,CallbackQueryHandler
cmd_folder = os.path.realpath(os.path.dirname(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0])))
import urllib

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from transitions.extensions import MachineFactory
from IPython.display import Image, display, display_png


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
                                    model = self,
                                    **machine_configs
                                    )
    def show_graph(self, **kwargs):
        self.get_graph(**kwargs).draw('state.png', prog='dot')
        display(Image('state.png'))
    
    
    
    def is_going_to_state6(self, update):
        text = update.message.text
        return text.lower() == 'g'
    def is_going_to_state6to7(self, update):
        text = update.message.text
        return text.lower() == 'h'
    def is_going_to_state7to8(self, update):
        text = update.message.text
        return text.lower() == 'i'
    
    def on_enter_state6(self, update):
        update.message.reply_text("state6")
    def on_enter_state7(self, update):
        update.message.reply_text("state7")
    def on_enter_state8(self, update):
        update.message.reply_text("state8")
        self.go_back(update)
    
    
    
    
    
    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'a'
    
    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'z'
    
    def is_going_to_state1to3(self, update):
        text = update.message.text
        return text.lower() == 'c'
    
    def is_going_to_state3to1(self, update):
        text = update.message.text
        return text.lower() == 'd'
    
    def is_going_to_state3to4(self, update):
        text = update.message.text
        return text.lower() == 'e'
    def is_going_to_state4to5(self, update):
        text = update.message.text
        return text.lower() == 'f'
    
    
    def on_enter_state3(self, update):
        update.message.reply_text("state3")
        update.message.reply_photo('https://telegram.org/img/t_logo.png')
    
    def on_exit_state3(self, update):
        print('Leaving state3')
    
    def on_enter_state4(self, update):
        update.message.reply_text("state4")
        self.go_back(update)
    
    def on_enter_state5(self, update):
        update.message.reply_text("state5")
        self.go_back(update)
    
    def on_enter_state1(self, update):
        update.message.reply_text("state1")
        self.sendMessage(parse_mode='https://www.google.com.tw/')
    
        
    
    def on_exit_state1(self, update):
        print('Leaving state1')
    
    def on_enter_state2(self, update):
        update.message.reply_text("state2")
        keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),InlineKeyboardButton("Option 2", callback_data='2')],[InlineKeyboardButton("Option 3", callback_data='3')]]
    
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Please choose:', reply_markup=reply_markup)
        
        
        update.message.reply_audio('https://www.w3schools.com/html/mov_bbb.mp4')
        
        
        
        self.go_back(update)
    
    
    def button(self, update):
        query = update.callback_query
        self.edit_message_text(text="Selected option: %s" % query.data,chat_id=query.message.chat_id,message_id=query.message.message_id)
    
    
    def on_exit_state2(self, update):
        print('Leaving state2')
    
GraphMachine = MachineFactory.get_predefined(graph=True, nested=True)
