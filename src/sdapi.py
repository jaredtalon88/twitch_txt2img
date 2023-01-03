import httpx
import json

url = "http://127.0.0.1:7860/sdapi/v1/txt2img"

negative_prompt = "cropped, lowres, poorly drawn face, out of frame, poorly drawn hands, blurry, bad art, blurred, text, watermark, disfigured, deformed, closed eyes, nude, nudity, nsfw, gore, nipple, genital, blood"


async def call_sdapi(prompt=str):
    data = {
        "prompt": f"{prompt}",
        "negative_prompt": f"{negative_prompt}",
        "steps": "25",
        "sampler_index": "Euler a",
    }
    data_to_json = json.dumps(data)
    resp = httpx.post(url, data=data_to_json, timeout=None)
    if resp.status_code != 200:
        print(f"something went wrong: {str(resp.content)}")
    else:
        return resp
