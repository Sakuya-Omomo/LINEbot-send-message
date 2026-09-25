import os

from dotenv import load_dotenv
from linebot import LineBotApi
from linebot.models import TextSendMessage

load_dotenv()

CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")
USER_ID = os.getenv("USER_ID")

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)


def main():
    message = TextSendMessage(text="テスト一か月前だよ‼\nそろそろ勉強しよう!📚")

    line_bot_api.push_message(USER_ID,messages=message)

if __name__ == "__main__":
    main()