from twitchio.ext import commands
from dotenv import load_dotenv
from sdapi import call_sdapi
from image_helper import save_image, open_browser
import os
from selenium import webdriver
from os.path import exists


if exists("init.txt"):
    print("Must delete init.txt")
    exit()

load_dotenv()

driver = webdriver.Chrome(service_log_path="")


bot = commands.Bot(
    irc_token=os.environ["TMI_TOKEN"],
    client_id=os.environ["CLIENT_ID"],
    nick=os.environ["BOT_NICK"],
    prefix=os.environ["BOT_PREFIX"],
    initial_channels=[os.environ["CHANNEL"]],
)


@bot.event
async def event_ready():
    print("logging into " + os.environ["CHANNEL"] + "'s channel")


@bot.command(name="img")
async def img(ctx):
    name = ctx.author.name.lower()
    msg = ctx.content.lower()
    prompt = msg.removeprefix("!img ")
    print(f"Prompt is: {prompt}")
    resp = await call_sdapi(prompt)
    image_name = await save_image(resp.json())
    await open_browser(driver)
    return


if __name__ == "__main__":
    bot.run()
