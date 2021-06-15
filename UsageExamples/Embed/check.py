from discord.ext import embed as eembed

embed = eembed.Embed(
    ...
)


"""
return value

type: dict

r['r'] -> return code (0 / 1)
    0 - success
    1 - failed

r['e'] -> error info (List[dict])
    r['e']['n'] -> error name
    r['e']['r'] -> error reason
"""

r = embed.check()
r = embed.check(raise_e=False)
