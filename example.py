from discord.ext import embed as eembed
from datetime import datetime
from typing import Optional, Any, List
from discord import Colour


embed = eembed.Embed(
    title = 'title',
    description = 'description',
    url = 'https://something.url/',
    color = 0x00ffff,
    # colour=discord.Colour.blue()
    timestamp = datetime.now(),
    author = {
        "name": "author name",
        "url": "https://author.twitter.com/",
        "icon_url": "https://something_image_url.png"
    },
    footer = {
        "text": "footer text",
        "icon_url": "https://something_footer_image_url.png"
    },
    image = 'https://image.png',
    thumbnail = 'https://thumbnail.png',
    fields = [
        {
            "name": "first field name",
            "value": "first field value"
        },
        {
            "name": "second field name",
            "value": "second field value",
            "inline": False
        }
    ]
)
