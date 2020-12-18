import json
import os
import re
import unicodedata

import dotenv
import twitchio
from twitchio.ext import commands

dotenv.load_dotenv()


def denoise(content):
    nfkc = unicodedata.normalize("NFKC", content)

    result = ""
    for char in nfkc:
        if unicodedata.combining(char) == 0:
            result += char.lower()

    return result


filters = {}
with open("./filters.json") as fp:
    for channel, terms in json.load(fp).items():
        filters[channel.lower()] = [
            (
                term,
                re.compile(r"\b" + re.escape(denoise(term)) + r"\b"),
            )
            for term in terms
        ]


bot = commands.Bot(
    nick=os.getenv("IRC_NICK").lower(),
    irc_token=os.getenv("IRC_TOKEN"),
    client_id=os.getenv("CLIENT_ID"),
    initial_channels=list(filters.keys()),
    prefix=[],
)


@bot.event
async def event_message(message: twitchio.Message):
    if message.author.is_mod:
        return

    denoised = denoise(message.content)
    for term, term_re in filters[message.channel.name]:
        if term_re.search(denoised):
            await message.channel.timeout(
                message.author.name,
                reason=f"used blocked term {term!r}",
            )
            return


bot.run()
