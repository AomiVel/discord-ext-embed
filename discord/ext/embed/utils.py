def Field(name, value, inline=True):
    return dict(name=str(name), value=str(value), inline=inline)

def Footer(text=None, icon_url=None):
    result = {}
    if text:
        result['text'] = str(text)
    if icon_url:
        result['icon_url'] = str(icon_url)
    return result

def Author(name, url=None, icon_url=None):
    result = {'name': str(name)}
    if url:
        result['url'] = str(url)
    if icon_url:
        result['icon_url'] = str(icon_url)
    return result
