from typing import (
    Union,
    Optional,
    Any,
    List,
    Dict
)

from discord import (
    Colour as disColour,
    Embed as disEmbed
)

from datetime import (
    datetime as dt,
    timezone as tz
)

from .fake_typehint import (
    discord,
    datetime
)


class Embed:
    slots = (
        'title',
        'type',
        'description',
        'url',
        'timestamp',
        'color',
        'image',
        'thumbnail',
        
        'author',
        'footer',
        'fields'
    )
    types = (
        'rich',
        'image',
        'video',
        'gifv',
        'article',
        'link'
    )
    
    def __init__(self, *,
        title: Optional[Any] = None,
        type: Optional[str] = 'rich',
        description: Optional[Any] = None,
        url: Optional[str] = None,
        timestamp: Optional[datetime.datetime] = None,
        colour: Optional[Union[int, discord.Colour]] = None,
        color: Optional[Union[int, discord.Colour]] = None,
        
        footer: Optional[dict] = None,
        image: Optional[str] = None,
        thumbnail: Optional[str] = None,
        author: Optional[dict] = None,
        fields: Optional[List[dict]] = None
        ):
        
        if not type in self.types:
            raise ValueError('type not in supported types')
            
        self.type = type
        self.title = title
        self.description = description
        self.url = url
        
        if color:
            if not color.__class__ in [int, disColour]:
                raise TypeError('color type must be int or discord.Colour not {0.__class__.__module__}.{0.__class__.__name__}'.format(color))
        if colour:
            if not colour.__class__ in [int, disColour]:
                raise TypeError('colour type must be int or discord.Colour not {0.__class__.__module__}.{0.__class__.__name__}'.format(colour))
            
        self.color = self.colour = color if color is not None else colour
        self.image = image
        self.thumbnail = thumbnail
        
        if timestamp:
            if not isinstance(timestamp, dt):
                raise TypeError('timestamp type must be datetime.datetime not {0.__class__.__module__}.{0.__class__.__name__}'.format(timestamp))
        self.timestamp = timestamp
        
        self.footer = None
        if footer:
            footer = self._to_correct(footer, 'footer')
            self.footer = footer
        
        self.author = None
        if author:
            author = self._to_correct(author, 'author')
            self.author = author
        
        self.fields = None
        if fields:
            fields = self._to_correct(fields, 'fields')
            self.fields = fields
    
    def __len__(self):
        total = 0
        if self.title:
            total += len(self.title)
        if self.description:
            total += len(self.description)
        for f in self.fields:
            total += len(str(f['name'])) + len(str(f['value']))
        if self.footer:
            total += len(str(self.footer['text']))
        if self.author:
            total += len(str(self.author['name']))
        return total
    
    
    def _to_correct(self, obj, name):
        if name == 'footer':
            if not isinstance(obj, dict):
                raise TypeError('footer type must be dict not {0.__class__.__module__}.{0.__class__.__name__}'.format(obj))
            
            result = {}
            text = obj.get('text')
            icon_url = obj.get('icon_url')
            
            if name:
                result['text'] = text
            
            if icon_url:
                result['icon_url'] = icon_url
            
            return result
        
        if name == 'author':
            if not isinstance(obj, dict):
                raise TypeError('author type must be dict not {0.__class__.__module__}.{0.__class__.__name__}'.format(obj))
            
            if not 'name' in obj.keys():
                raise KeyError("author missing required key: 'name'")
                
            result = {
                'name': obj['name']
            }
            url = obj.get('url')
            icon_url = obj.get('icon_url')
            
            if url:
                result['url'] = url
            
            if icon_url:
                result['icon_url'] = icon_url
            
            return result
        
        if name == 'fields':
            if not any((isinstance(obj, list), isinstance(obj, tuple))):
                raise TypeError('fields type must be list or tuple not {0.__class__.__module__}.{0.__class__.__name__}'.format(obj))
            
            result = []
            for field in obj:
                if not isinstance(field, dict):
                    raise TypeError('field type must be dict not {0.__class__.__module__}.{0.__class__.__name__}'.format(field))
                
                if not 'name' in field.keys():
                    raise KeyError("field missing required key: 'name'")
                
                if not 'value' in field.keys():
                    raise KeyError("field missing required key: 'value'")
                
                name = field['name']
                value = field['value']
                inline = field.get('inline', True)
                
                _res = {
                    'name': name,
                    'value': value,
                    'inline': inline
                }
                result.append(_res)
            
            return result
    
    
    def check(self, raise_e=True):
        errors = {
            'r': 0,
            'e': []
        }
        
        if not self.type in self.types:
            if raise_e:
                raise ValueError('type not in supported types')
            else:
                errors['r'] = 1
                errors['e'].append({'n': 'type', 'r': 'type not in supported types'})
        
        if not type(self.color) in (int, disColour, None):
            if raise_e:
                raise TypeError('color type must be int or discord.Colour not {0.__class__.__module__}.{0.__class__.__name__}'.format(self.color))
            else:
                errors['r'] = 1
                errors['e'].append({'n': 'color', 'r': 'color type must be int or discord.Colour not {0.__class__.__module__}.{0.__class__.__name__}'.format(self.color)})
                
        if not type(self.colour) in (int, disColour, None):
            if raise_e:
                raise TypeError('colour type must be int or discord.Colour not {0.__class__.__module__}.{0.__class__.__name__}'.format(self.color))
            else:
                errors['r'] = 1
                errors['e'].append({'n': 'colour', 'r': 'colour type must be int or discord.Colour not {0.__class__.__module__}.{0.__class__.__name__}'.format(self.colour)})
        
        if not self.footer is None:
            if not isinstance(self.footer, dict):
                if raise_e:
                    raise TypeError('footer type must be dict not {0.__class__.__module__}.{0.__class__.__name__}'.format(self.footer))
                else:
                    errors['r'] = 1
                    errors['e'].append({'n': 'footer', 'r': 'footer type must be dict not {0.__class__.__module__}.{0.__class__.__name__}'.format(self.footer)})
        
        if not self.author is None:
            e = []
            eb = False
            if not isinstance(self.author, dict):
                if raise_e:
                    raise TypeError('author type must be dict not {0.__class__.__module__}.{0.__class__.__name__}'.format(self.author))
                else:
                    errors['r'] = 1
                    e.append('author type must be dict not {0.__class__.__module__}.{0.__class__.__name__}'.format(self.author))
                    eb = True
                
            if not 'name' in self.author.keys():
                if raise_e:
                    raise KeyError("author missing required key: 'name'")
                else:
                    errors['r'] = 1
                    e.append("author missing required key: 'name'")
                    eb = True
            
            if eb:
                errors['e'].append({'n': 'author', 'r': e})
        
        if not self.fields is None:
            e = []
            eb = False
            if not any((isinstance(self.fields, list), isinstance(self.fields, tuple))):
                if raise_e:
                    raise TypeError('fields type must be list or tuple not {0.__class__.__module__}.{0.__class__.__name__}'.format(self.fields))
                else:
                    errors['r'] = 1
                    e.append('fields type must be list or tuple not {0.__class__.__module__}.{0.__class__.__name__}'.format(self.fields))
                    eb = True
            
            for field in self.fields:
                if not isinstance(field, dict):
                    if raise_e:
                        raise TypeError('field type must be dict not {0.__class__.__module__}.{0.__class__.__name__}'.format(field))
                    else:
                        errors['r'] = 1
                        e.append('field type must be dict not {0.__class__.__module__}.{0.__class__.__name__}'.format(field))
                        eb = True
                    
                    
                if not 'name' in field.keys():
                    if raise_e:
                        raise KeyError("field missing required key: 'name'")
                    else:
                        errors['r'] = 1
                        e.append("field missing required key: 'name'")
                        eb = True
                
                if not 'value' in field.keys():
                    if raise_e:
                        raise KeyError("field missing required key: 'value'")
                    else:
                        errors['r'] = 1
                        e.append("field missing required key: 'value'")
                        eb = True
            
            if eb:
                errors['e'].append({'n': 'fields', 'r': e})
        
        return errors
    
    def to_dict(self):
        result = {'type': self.type}

        if self.title:
            result['title'] = str(self.title)
        if self.description:
            result['description'] = str(self.description)
        if self.url:
            result['url'] = str(self.url)
        if self.timestamp:
            timestamp = self.timestamp
            if timestamp.tzinfo is None:
                timestamp = timestamp.astimezone()
            if timestamp.tzinfo:
                result['timestamp'] = timestamp.astimezone(tz=tz.utc).isoformat()
            else:
                result['timestamp'] = timestamp.replace(tzinfo=tz.utc).isoformat()
        if self.color or self.colour:
            color = self.color if self.color is not None else self.colour

            if isinstance(color, disColour):
                color = color.value
            result['color'] = color
        if self.image:
            result['image'] = {
                'url': str(self.image)
            }
        if self.thumbnail:
            result['thumbnail'] = {
                'url': str(self.thumbnail)
            }
        if self.author:
            name = str(self.author['name'])
            url = self.author.get('url')
            icon_url = self.author.get('icon_url')
            author = {'name': name}
            if url:
                author['url'] = str(url)
            if icon_url:
                author['icon_url'] = str(icon_url)

            result['author'] = author
        if self.footer:
            text = self.footer.get('text')
            icon_url = self.footer.get('icon_url')

            footer = {}
            if text:
                footer['text'] = str(text)
            if icon_url:
                footer['icon_url'] = str(icon_url)

            result['footer'] = footer
        if self.fields:
            res = []
            for field in self.fields:
                f = {
                    'name': str(field['name']),
                    'value': str(field['value']),
                    'inline': field.get('inline', True)
                }
                res.append(f)
            result['fields'] = res
        
        return result
    
    @classmethod
    def from_dict(cls, data):
        result = {}
        for key in data.keys():
            if data[key]:
                if key == 'image':
                    result['image'] = data[key]['url']
                elif key == 'thumbnail':
                    result['thumbnail'] = data[key]['url']
                else:
                    result[key] = data[key]
        return cls(**result)
    
    def to_discordEmbed(self):
        return disEmbed.from_dict(self.to_dict())
    
    @classmethod
    def from_discordEmbed(cls, data):
        return cls.from_dict(data.to_dict())
    
    
    def add_field(self, *, name: Any, value: Any, inline: Optional[bool] = True):
        self.fields.append(
            dict(
                name=str(name),
                value=str(value),
                inline=inline
            )
        )
    def add_fields(self, fields: List[dict]):
        for field in fields:
            self.fields.append(
                dict(
                    name=str(field['name']),
                    value=str(field['value']),
                    inline=field.get('inline', True)
                )
            )
    def set_field(self, index, *, name: Any, value: Any, inline: Optional[bool] = True):
        self.fields[index] = dict(
            name=str(name),
            value=str(value),
            inline=inline
        )
    def remove_field(self, index: int):
        del self.fields[int(index)]
    def remove_fields(self, *indexes):
        for index in sorted(indexes, reverse=True):
            del self.fields[int(index)]
    def clear_fields(self):
        self.fields = None
    
    def set_image(self, url: str):
        self.image = str(url)
    def remove_image(self):
        self.image = None
    
    
    def set_thumbnail(self, url: str):
        self.thumbnail = str(url)
    def remove_thumbnail(self):
        self.thumbnail = None
    
    
    def set_footer(self, *, text: Optional[Any] = None, icon_url: Optional[str] = None):
        res = {}
        if text:
            res['text'] = str(text)
        if icon_url:
            res['icon_url'] = icon_url
        self.footer = res
    def remove_footer(self):
        self.footer = None
    
    def set_author(self, *, name: Any, url: Optional[str] = None, icon_url: Optional[str] = None):
        res = dict(
            name=str(name)
        )
        if url:
            res['url'] = str(url)
        if icon_url:
            res['icon_url'] = str(icon_url)
        self.author = res
    def remove_author(self):
        self.author = None
