# pip install requests
# get API key from https://www.thetextapi.com
# imports
import requests
import json
from config import apikey
# create headers
headers = {
    "Content-Type": "application/json",
    "apikey": apikey
}
# create keywords
keywords = ["fuck", "damn", "shit", "sexual assault", "rape", "gun"]
# url
url = "https://app.thetextapi.com/text/sentences_with_keywords"

moderation = {
    0: "safe",
    1: "13+"
}
# create function
def moderate(text: str):
    # create the body from the text
    body = {
        "text": text,
        "keywords": keywords
    }
    # pass in with keywords
    response = requests.post(url=url, headers=headers, json=body)
    # receive response and check for returned sentences
    _dict = json.loads(response.text)

    # grade returned sentences for 13+, 18+
    rating = 0
    mod_status = ""
    for kw in keywords[:3]:
        rating += len(_dict[kw])
    if rating in moderation:
        mod_status = moderation[rating]
    else:
        mod_status = "18+"
    
    # grade for trigger warning
    triggers = 0
    trigger_warning = False
    for kw in keywords[3:]:
        triggers += len(_dict[kw])
    if triggers > 0:
        trigger_warning = True
    
    # return response
    return mod_status, trigger_warning

# print(moderate("this is a safe text")) # safe, false
# print(moderate("this text fuck samuel l jackson says. Fuck you once in a rated r movie is 18")) # 18+, false
# print(moderate("this is fuck 13+")) # 13+, false
# print(moderate("this is a trigger warning gun")) # safe, true 