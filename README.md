# Virtual-Farmer-Autobot
Python script that automatically plays Virtual Farmer for you!

## What is Virtual Farmer? [Source](https://virtualfarmerbot.com/)
Virtual Farmer is a Discord minigame, that is *"focused on farming, there are countless plants, tools, and upgrades for you to discover. Your progress in the bot stays with you across servers, allowing you to farm wherever you'd like and still show off to your friends in another server."*

## What does this "autobot" do?
My "autobot" (yeah, I don't have better name for it) farms and sells resources, and also solves AntiBot measures (ha!).
___
# How to use?
For this bot to run properly, you'll need 5 things:
- Virtual Farmer (obviously)
- your Discord User Token
- custom Discord Bot Token
- Message URL
- User ID

### Obtaining Discord User Token
1. You can follow this guide: https://linuxhint.com/get-discord-token/
2. Put your Discord User Token inside the script to "userToken" field inside quotation marks

### Obtaining Discord Bot Token | Edited for specific purpose from [this source](https://discordpy.readthedocs.io/en/stable/discord.html)
1. Make sure you’re logged on to the [Discord website](https://discord.com/)
2. Navigate to the [application page](https://discord.com/developers/applications)
3. Click on the “New Application” button
4. Give the application a name (e.g. "Virutal Farmer Exploit") and click “Create”
5. Navigate to the “Bot” tab to configure it
6. Make sure that **Message Content Intent** is ticked
7. Copy the token using the “Copy” button
8. Put copied token inside the script to "botToken" field inside quotation marks
9. Go to the “OAuth2 > URL Generator” tab
10. Tick the “bot” checkbox under “scopes”
11. Tick the "Read Message/View Channels" checkbox under “Bot Permissions”
12. Copy and paste the URL into your browser, choose a server to invite the bot to, and click “Authorize”

### Obtaining Message URL
Run "/play" in server chat to start playing Virtual Farmer, right click the message and click "Copy Message Link" and paste it inside the script to "message_url" field inside quotation marks

### Obtaining User ID
1. Enable Developer Mode in *User Settings > Advanced*
2. Go to any chat, right click your nickname, click on "Copy User ID" and paste it inside the script to "user_id" field inside quotation marks

## After obtaining everything you need
After you've done everything prior to this paragraph, simply run this bot using `python3 VitualFarmerAutobot.py`
