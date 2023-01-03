## How to do in TikTok

```python
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent
client: TikTokLiveClient = TikTokLiveClient(unique_id="@REPLACE_ME")


@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)


async def on_comment(event: CommentEvent):
    if event.comment.startswith("!img"):
        prompt = event.comment.removeprefix("!img ")
        print(f"Prompt received: {prompt}")
        resp = call_sdapi(prompt)
        image_name = save_image(resp.json())
        open_browser()
    return


# Define handling an event via "callback"
 client.add_listener("comment", on_comment)

if __name__ == "__main__":
    client.run()
```