# (c) @PredatorHackerzZ || @TeleRoidGroup

import os


class Config(object):
	API_ID = 18424928
	API_HASH = "d12e98533ee6d6222e63dac56c504913"
	BOT_TOKEN = "5972704618:AAHNV97qrU38FOBXAhQUJ8jj6sufcNwWpr4"
	BOT_USERNAME = "ellisa_files_bot"
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001728534546"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1017302540"))
	DATABASE_URL = "mongodb+srv://Irfan:786or786@cluster0.2jjhd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001517118352")
	LOG_CHANNEL = "-1001794573996"
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
**My Name:** [𝐅𝐢𝐥𝐞 𝐒𝐭𝐨𝐫𝐞 𝐁𝐨𝐭](https://t.me/{BOT_USERNAME})

**Language:** [𝐏𝐲𝐭𝐡𝐨𝐧𝟑](https://www.python.org)

**Library:** [𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦](https://docs.pyrogram.org)

**Hosted On:** [𝐕𝐏𝐒](https://t.me/ellisa_support)

**Developer:** [Danger](https://t.me/ellisa_support) 

**Bot Support:** [𝐒𝐮𝐩𝐩𝐨𝐫𝐭](https://t.me/ellisa_support_group)

**Bot Updates:** [𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/ellisa_world)
"""
	ABOUT_DEV_TEXT = f"""
**𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [Danger](https://t.me/ellisa_support) 

𝐈𝐟 𝐘𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐃𝐨𝐧𝐚𝐭𝐞 𝐎𝐮𝐫 𝐇𝐚𝐫𝐝 𝐖𝐨𝐫𝐤. 𝐘𝐨𝐮 𝐂𝐚𝐧 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐓𝐡𝐞 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫. 
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

Send me any File & It will be uploaded in My Database & You will Get the File Link.

Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
