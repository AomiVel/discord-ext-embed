""" YOU MUST USE NAME """

""" import """
from discord.ext import embed
# or
from discord.ext.embed import utils


""" use """

embed.utils.Author
embed.Author

utils.Author


# Use name only
embed.Embed(
    author=utils.Author('author name')
)


# Use name and url
embed.Embed(
    author=utils.Author('author name', 'https://author.url/')
)

# Use name and icon_url
embed.Embed(
    author=utils.Author('author name', icon_url='https://author-icon.url/')
)
embed.Embed(
    author=utils.Author('author name', None, 'https://author-icon.url/')
)


# use all
embed.Embed(
    author=utils.Author('author name', 'https://author.url/', 'https://author-icon.url/')
)
