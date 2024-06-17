import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


# Discord client
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def getnews(ctx):
    # Setup Selenium WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (without opening browser window)
    driver = webdriver.Chrome(options=chrome_options)

    url = 'https://www.yahoo.com/tagged/artificial-intelligence/'
    scraped_data_class_1 = scrape_yahoo_ai_news_class_1(driver, url)
    scraped_data_class_2 = scrape_yahoo_ai_news_class_2(driver, url)

    # Send scraped news to Discord
    for news_item in scraped_data_class_1:
        embed = discord.Embed(title=news_item['headline'], url=news_item['link'], color=discord.Color.blue())
        embed.set_image(url=news_item['image_url'])
        await ctx.send(embed=embed)

    for news_item in scraped_data_class_2:
        embed = discord.Embed(title=news_item['headline'], url=news_item['link'], color=discord.Color.blue())
        embed.set_image(url=news_item['image_url'])
        await ctx.send(embed=embed)

    # Quit Selenium WebDriver
    driver.quit()

def scrape_yahoo_ai_news_class_1(driver, url):
    driver.get(url)
    time.sleep(2)  # Let the page load

    # Find all li elements under the specified ul container
    items = driver.find_elements_by_css_selector('ul.common.simple-list.Pstart(0) > li')
    scraped_data = []

    # Loop through each li element
    for item in items:
        headline = item.find_element_by_tag_name('a').text.strip()
        link = item.find_element_by_tag_name('a').get_attribute('href')
        image_element = item.find_element_by_tag_name('img')
        image_url = image_element.get_attribute('src') if image_element else None
        scraped_data.append({'headline': headline, 'link': link, 'image_url': image_url})

    return scraped_data

def scrape_yahoo_ai_news_class_2(driver, url):
    driver.get(url)
    time.sleep(2)  # Let the page load

    # Find all li elements under the specified ul container
    items = driver.find_elements_by_css_selector('ul.common.simple-list.Pstart(0).D(f).Flw(w).Jc(fs).List(n).Mx(-10px) > li')
    scraped_data = []

    # Loop through each li element
    for item in items:
        headline = item.find_element_by_tag_name('a').text.strip()
        link = item.find_element_by_tag_name('a').get_attribute('href')
        image_element = item.find_element_by_tag_name('img')
        image_url = image_element.get_attribute('src') if image_element else None
        scraped_data.append({'headline': headline, 'link': link, 'image_url': image_url})

    return scraped_data

bot.run('')
