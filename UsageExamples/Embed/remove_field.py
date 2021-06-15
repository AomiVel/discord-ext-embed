from discord.ext import embed as eembed

embed = eembed.Embed(
    fields = [
        dict(
            name='first field',
            value='first field'
        ),
        dict(
            name='second field',
            value='second field'
        )
    ]
)


"""
pprint.pprint(embed.fields)

> [{'inline': True, 'name': 'first field', 'value': 'first field'},
> {'inline': True, 'name': 'second field', 'value': 'second field'}]
"""

embed.remove_field(0)

"""
pprint.pprint(embed.fields)

> [{'inline': True, 'name': 'second field', 'value': 'second field'}]
"""
