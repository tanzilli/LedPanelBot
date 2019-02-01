# LedPanelBot

<img src="https://telegram.org/file/811140058/2/7GzMJk4Ij54/a1649c56fa9f805828">

Examples of Telegram bot written in Python

## Installing

	sudo apt update
	sudo apt install python-setuptools
	sudo apt install git
	sudo apt-get install python-pip
	sudo apt install libffi-dev
	sudo apt-get install  libssl-dev
	
	pip install python-telegram-bot

Clone the whole repository with:
	
	cd
	git clone https://github.com/tanzilli/LedPanelBot
	cd LedPanelBot

or copy only the source you need.

## Running

Create your own bot with <https://telegram.me/BotFather> using your Telegram
client then use the token you got inside the bot source example:

	updater = telegram.ext.Updater("insert your bot token here")	
	
Launch the bot by typing:

	python ledpanelbot.py	


