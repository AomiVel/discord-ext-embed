""" YOU MUST USE NAME AND VALUE """

""" import """
from discord.ext import embed
# or
from discord.ext.embed import utils


""" use """

embed.utils.Field
embed.Field

utils.Field


# Don't use inline
embed = embed.Embed(
    fields=[
        utils.Field('The name of the field', 'The value of the value')
    ]
)


# Use inline
embed = embed.Embed(
    fields=[
        utils.Field('The name of the field', 'The value of the value', False)
    ]
)
