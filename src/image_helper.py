import io
import base64
from PIL import Image, PngImagePlugin
import webbrowser
from os.path import exists
import time


async def save_image(payload):
    for entry in payload["images"]:
        image = Image.open(io.BytesIO(base64.b64decode(entry.split(",", 1)[0])))
        image.save("newimage.png")
        print("new image saved")
    return


async def open_browser(driver):
    url = "file:///C:/Users/jay/python/twitch_txt2img/src/newimage.png"
    # only open chrome once, if its open already, just refresh
    not_first_image = exists("init.txt")
    if not_first_image:
        driver.get(driver.current_url)
        driver.refresh()
    else:
        with open("init.txt", "w") as init_file:
            pass
        driver.get(url)
    return
