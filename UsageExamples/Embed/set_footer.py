from discord.ext import embed as eembed

embed = eembed.Embed()

"""
print(embed.footer)

> None
"""

embed.set_footer(text='footer text', icon_url='https://embed-footer-icon.url/')

"""
print(embed.footer)

> {'text': 'footer text', 'icon_url': 'https://embed-footer-icon.url/'}
