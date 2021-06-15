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

embed.set_field(
    1,
    name='set field name',
    value='set field value'
)

"""
pprint.pprint(embed.fields)
> [{'inline': True, 'name': 'first field', 'value': 'first field'},
> {'inline': True, 'name': 'set field name', 'value': 'set field value'},
> {'inline': True, 'name': 'third field', 'value': 'third firld'}]
"""
