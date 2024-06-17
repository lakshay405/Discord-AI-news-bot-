# Discord-AI-news-bot-
Discord News Bot
This Discord bot scrapes news articles related to artificial intelligence from Yahoo News and sends them as embeds to a Discord channel.

Features
Web Scraping: Utilizes Selenium with Chrome WebDriver to scrape news articles from Yahoo News.
Discord Integration: Sends scraped news articles as embeds to a Discord channel upon command.
Headless Browser: Runs Selenium WebDriver in headless mode to scrape data without launching a browser window.
Requirements
Python 3.6+
discord.py
selenium
Chrome WebDriver
Setup and Installation
Clone the repository:
git clone https://github.com/yourusername/discord-news-bot.git
cd discord-news-bot
Download Chrome WebDriver:

Download Chrome WebDriver from here and place it in your PATH or specify the path in your code.
Configure bot token:

Replace bot.run('YOUR_BOT_TOKEN') with your Discord bot token in bot.py.
python bot.py

Usage
After setting up and running the bot, use the command !getnews in your Discord server to fetch and display the latest AI news articles from Yahoo News.
File Structure
bot.py: Main script containing the Discord bot implementation.
chromedriver: Chrome WebDriver executable.
requirements.txt: List of Python dependencies.
