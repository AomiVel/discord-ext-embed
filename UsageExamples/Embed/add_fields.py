from discord.ext import embed as eembed

embed = eembed.Embed(
    ...
)

embed.add_fields(
    {
        "name": "The name of the field",
        "value": "The value of the field. inline: True"
    },
    {
        "name": "The name of the field",
        "value": "The value of the field. inline: False",
        "inline": False
    },
    
    dict(
        name="The name of the field",
        value="The value of the field. inline: True"
    ),
    dict(
        name="The name of the field",
        value="The value of the field. inline: False",
        inline=False
    )
)
