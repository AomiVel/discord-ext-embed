from discord.ext import embed as eembed

embed = eembed.Embed(
    author=dict(
        name='author name',
        url='https://author.url/',
        icon_url='https://author-icon.url/'
    )
)

"""
print(embed.author)

> {'name': 'author name', 'url': 'https://author.url/', 'icon_url': 'https://author-icon.url/'}
"""

embed.remove_author()

"""
print(embed.author)

> None
"""
