""" import """
from discord.ext import embed
# or
from discord.ext.embed import utils


""" use """

embed.utils.Footer
embed.Footer

utils.Footer


# Use text only
embed = embed.Embed(
    footer=utils.Footer('The text of the footer')
)


# Use icon_url only
embed = embed.Embed(
    footer=utils.Footer(icon_url='https://footer-icon.url/')
)
embed = embed.Embed(
    footer=utils.Footer(None, 'https://footer-icon.url/')
)


# Use all
embed = embed.Embed(
    footer=utils.Footer('The text of the footer', 'https://footer-icon.url/')
)
