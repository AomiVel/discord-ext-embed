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
        ),
        dict(
            name='third field',
            value='third firld'
        )
    ]
)

"""
pprint.pprint(embed.fields)

> [{'inline': True, 'name': 'first field', 'value': 'first field'},
> {'inline': True, 'name': 'second field', 'value': 'second field'},
> {'inline': True, 'name': 'third field', 'value': 'third firld'}]
"""


embed.remove_fields(0, 2)

"""
pprint.pprint(embed.fields)

> [{'inline': True, 'name': 'second field', 'value': 'second field'}]
"""
