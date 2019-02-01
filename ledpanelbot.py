#!/usr/bin/env python
 
import telegram.ext
import logging

import time
import os

video_keyboard = telegram.ReplyKeyboardMarkup([["VIDEO1","VIDEO2","VIDEO3","VIDEO4"],["STOP"]])
video_keyboard.one_time_keyboard=False
video_keyboard.resize_keyboard=True

current_command="play"

screen = None
		
# Enable logging
logging.basicConfig(
		format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
		level=logging.INFO)

logger = logging.getLogger(__name__)

def cmd_start(bot, update):
	bot.sendMessage(update.message.chat_id, "Ciao %s ! Io sono LedPanelBot. \n" % ( update.message.from_user.first_name))
	bot.sendMessage(update.message.chat_id, text="Seleziona un video per farne il play ...", reply_markup=video_keyboard)

def cmd_play(bot, update):
	global current_command	
	bot.sendMessage(update.message.chat_id, text="Che video vuoi riprodurre ?", reply_markup=video_keyboard)
	current_command="play"
	
def cmd_delete(bot, update):
	pass

def cmd_cancel(bot, update):
	global current_command
	current_command=None
	bot.sendMessage(update.message.chat_id, text="Comando cancellato")
	
def message_handler(bot, update):
	global current_command
	global screen
	
	print "Ricevuto un messagio"
	print "----> Mittente: : [" + update.message.from_user.username + "]"
	print "      Testo     : [" + update.message.text + "]"
	print current_command
 
	#print update.message
 
	if current_command=="save":
		if update.message.text=="VIDEO1":
			os.system("mv -f newvideo.mov video1.mov")
			current_command="play"

		if update.message.text=="VIDEO2":
			os.system("mv -f newvideo.mov video2.mov")
			current_command="play"

		if update.message.text=="VIDEO3":
			os.system("mv -f newvideo.mov video3.mov")
			current_command="play"

		if update.message.text=="VIDEO4":
			os.system("mv -f newvideo.mov video4.mov")
			current_command="play"

	if current_command=="play":
		if update.message.text=="VIDEO1":
			if os.path.exists("video1.mov"):
				os.system("sudo pkill omxplayer")
				os.system("omxplayer --win 0,0,256,640 --orientation 0 -o local --loop video1.mov &")
			else:
				bot.sendMessage(update.message.chat_id, "Il video non esiste")
						
		if update.message.text=="VIDEO2":
			if os.path.exists("video2.mov"):
				os.system("sudo pkill omxplayer")
				os.system("omxplayer --win 0,0,256,640 --orientation 0 -o local --loop video2.mov &")
			else:
				bot.sendMessage(update.message.chat_id, "Il video non esiste")

		if update.message.text=="VIDEO3":
			if os.path.exists("video3.mov"):
				os.system("sudo pkill omxplayer")
				os.system("omxplayer --win 0,0,256,640 --orientation 0 -o local --loop video3.mov &")
			else:
				bot.sendMessage(update.message.chat_id, "Il video non esiste")

		if update.message.text=="VIDEO4":
			if os.path.exists("video4.mov"):
				os.system("sudo pkill omxplayer")
				os.system("omxplayer --win 0,0,256,640 --orientation 0 -o local --loop video4.mov &")
			else:
				bot.sendMessage(update.message.chat_id, "Il video non esiste")

	if update.message.text=="STOP":
		os.system("sudo pkill omxplayer")

def video_handler(bot, update):
	global current_command
	print "Ricevuto un video"
	newFile = bot.getFile(update.message.video.file_id)
	newFile.download("newvideo.mov")
	bot.sendMessage(update.message.chat_id, text="Salva come VIDEO x ...", reply_markup=video_keyboard)
	current_command="save"

def document_handler(bot, update):
	global current_command
	print "Ricevuto un documento"
	newFile = bot.getFile(update.message.document.file_id)
	newFile.download("newvideo.mov")
	bot.sendMessage(update.message.chat_id, text="Salva come VIDEO x ...", reply_markup=video_keyboard)
	current_command="save"

def error(bot, update, error):
	logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():	
	global update_queue
	global screen
	
	#@LedPanelBot
	updater = telegram.ext.Updater("insert your bot token here")	
	
	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# Definisce gli handler di gestione dei comandi
	dp.add_handler(telegram.ext.CommandHandler("start",cmd_start))
	dp.add_handler(telegram.ext.CommandHandler("cancel",cmd_cancel))

	# Message handler
	dp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text,message_handler))

	# Video handler
	dp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.video,video_handler))

	# Document handler
	dp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.document,document_handler))

	# log all errors
	dp.add_error_handler(error)

	# Start the Bot
	update_queue = updater.start_polling()

	try:  
		# Run the bot until the you presses Ctrl-C or the process receives SIGINT,
		# SIGTERM or SIGABRT. This should be used most of the time, since
		# start_polling() is non-blocking and will stop the bot gracefully.
		updater.idle()

	except KeyboardInterrupt:  
		print "Exit"	

if __name__ == '__main__':
	main()
