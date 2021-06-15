from discord.ext import embed as eembed

embed = eembed.Embed(
    ...
)

embed.add_field(
    name='The name of the field',
    value='The value of the field. inline: True'
)

embed.add_field(
    name='The name of the field',
    value='The value of the field. inline: False',
    inline=False
)
