from cynanBot import CynanBot
from secrets import TWITCH_CLIENT_ID
from secrets import TWITCH_IRC_TOKEN
from secrets import TWITCH_PUB_SUB_TOKEN
from user import User

users = [
    User(
        twitchHandle = "Imyt",
        picOfTheDayFile = "/home/declan/potd.txt"
    ),
    User(
        twitchHandle = "smCharles",
        picOfTheDayFile = "/home/charles/potd.txt"
    )
]

cynanBot = CynanBot(
    ircToken = TWITCH_IRC_TOKEN,
    clientId = TWITCH_CLIENT_ID,
    users = users
)

print("Starting CynanBot...")
cynanBot.run()
