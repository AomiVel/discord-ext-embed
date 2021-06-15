from discord.ext import embed as eembed

embed = eembed.Embed(
    footer=dict(
        text='footer text',
        icon_url='https://embed-footer-icon.url/'
    )
)

"""
print(embed.footer)

> {'text': 'footer text', 'icon_url': 'https://embed-footer-icon.url/'}
"""

embed.remove_footer()

"""
print(embed.footer)

> None
