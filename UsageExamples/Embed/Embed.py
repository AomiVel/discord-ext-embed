from discord.ext import embed as eembed

embed = eembed.Embed(
    title = 'title',
    description = 'description',
    url = 'https://embed.url/',
    color = 0x00ffff,
    # colour=discord.Colour.blue()
    timestamp = datetime.now(),
    author = {
        "name": "author name",
        "url": "https://author.url/",
        "icon_url": "https://author-icon.url"
    },
    footer = {
        "text": "footer text",
        "icon_url": "https://footer-icon.url"
    },
    image = 'https://embed-image.url',
    thumbnail = 'https://embed-thumbnail.url',
    fields = [
        {
            "name": "first field",
            "value": "inline: True"
        },
        {
            "name": "second field",
            "value": "inline: False",
            "inline": False
        },
        dict(
            name='third field',
            value='inline: False',
            inline=False
        )
    ]
)
