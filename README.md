# [discord-ext-embed](https://github.com/AomiVel/discord-ext-embed)

discord.py >= 2.0.0


## install

```sh
$ git clone https://github.com/AomiVel/discord-ext-embed.git
$ cd discord-ext-embeds
$ python -m pip install -U .
```

## Easy Example

```py
from discord.ext import eembed
embed = eembed.Embed(
    title='Hello',
    description='World',
    author=dict(
        name='author name'
    ),
    fields=[
        dict(
            name='First field\'s name',
            value='First field\'s value'
        ),
        dict(
            name='Second field\'s name',
            value='Second field\'s value'
        )
    ]
)
```

## Reference

### ` class discord.ext.embed.Embed(**kwargs) `
#### Attributes
> author  
color  
description  
fields  
footer  
image  
thumbnail  
timestamp  
title  
type  
url

#### Methods
> def　add_field  
def　add_fields  
def　check  
def　clear_fields  
cls　from_dict  
cls　from_discordEmbed  
def　remove_author  
def　remove_field  
def　remove_fields  
def　remove_footer  
def　remove_image  
def　remove_thumbnail  
def　set_author  
def　set_field  
def　set_footer  
def　set_image  
def　set_thumbnail  
def　to_dict  
def　to_discordEmbed

#### Supported Operations
##### `len(x)`
Returns the total size of the embed. Useful for checking if it’s 
within the 6000 character limit.

---

##### `title`
The title of the embed.

**Type**: str

##### `type`
The type of the embed. Usually "rich". Possible strings for embed types can be found on discord’s [api docs](https://discord.com/developers/docs/resources/channel#embed-object-embed-types).  

**Type**: str

##### `description`
The description of the embed.  

**Type**: str

##### `url`
The URL of the embed.  

**Type**: str

##### `timestamp`
The timestamp of the embed content. This could be a naive or aware datetime.  

**Type**: datetime.datetime

##### `colour(color)`
The colour code of the embed. Aliased to `color` as well.  

**Type**: Union[int, discord.Colour]

##### `image`
The image URL of the embed.

**Type**: str

##### `thumbnail`
The thumbnail URL of the embed.

**Type**: str

##### `author`
The author of the embed.

**Type**: dict

##### `footer`
The footer of the embed.

**Type**: dict

##### `fields`
The fields of the embed.

**Type**: List[dict]

---

##### `check(raise_e=True)`
Check the information in the element is correct.

**Parameters**
> **raise_e**(bool) - Whether to raise an error

##### `to_dict()`
Converts this embed object into a dict.

##### `to_discordEmbed()`
Converts this embed object into a discord.Embed object.

##### `from_dict(data)`
Converts dict to a discord.ext.embed.Embed object provided it is in the format that Discord expects it to be in.

**Parameters**
> **data**(dict) - The dictionary to convert into an discord.ext.embed.Embed.

##### `from_discordEmbed(data)`
Converts discord.Embed to a discord.ext.embed.Embed object.

**Parameters**
> **data**(discord.Embed) - The discord.Embed to convert into an discord.ext.embed.Embed.

##### `add_field(*, name, value, inline=True)`
Adds a field to the embed object.

**Parameters**
> **name**(str) - The name of the field  
**value**(str) - The value of the field  
**inline**(bool) - Whether the field should be displayed inline.

##### `add_fields(*fields)`
Adds a fields to the embed object.

```py
embed.add_fields(
    {
        "name": "first field",
        "value": "inline is True"
    },
    
    dict(
        name="second field",
        value="inline is False",
        inline=False
    )
)
```

**Parameters**
> **fields**(dict) - Information about the field you want to add.

field example:
```py
{
    "name": "The name of the field",
    "value": "The value of the field",
    "inline": False
}
```

##### `set_field(index, *, name, value, inline=True)`
Set the field to the specified index in Embed.

**Parameters**
> **index**(int) - Index of the field that you wanna set.  
**name**(str) - The name of the field.  
**value**(str) - The value of the field.  
**inline**(bool) - Whether the field should be displayed inline.

##### `remove_field(index)`
Remove a field at the specified index.

**Parameters**
> **index**(int) - Index of the field that you wanna remove.

##### `remove_fields(*indexes)`
Remove a fields at the specified indexes.
Deleted from the highest value.

**Parameters**
> **indexes**(int) - Index of the fields that you wanna remove

##### `clear_fields()`
Clear the Embed fields.

##### `set_image(url)`
Sets the image for the embed content.

**Parameters**
> **url**(str) - The source URL for the image. Only HTTP(S) is supported.

##### `remove_image()`
Removes the image from the embed.

##### `set_thumbnail(url)`
Sets the thumbnail for the embed content.

**Parameters**
> **url**(str) - The source URL for the thumbnail. Only HTTP(S) is supported.

##### `remove_thumbnail()`
Removes the thumbnail from the embed.

##### `set_footer(*, text=None, icon_url=None)`
Sets the footer for the embed content.

**Parameters**
> **text**(str) - The footer text.  
**icon_url**(str) - The URL of the footer icon. Only HTTP(S) is supported.

##### `remove_footer()`
Removes the footer from the embed.

##### `set_author(*, name, url=None, icon_url=None)`
Sets the author for the embed content.

**Parameters**
> **name**(str) – The name of the author.  
**url**(str) – The URL for the author.  
**icon_url**(str) – The URL of the author icon. Only HTTP(S) is supported.

##### `remove_author()`
Clears embed’s author information.

### `utils`

#### `Field(name, value, inline=True)`
Help to create field dict.

**Parameters**

> **name**(str) - The name of the field  
**value**(str) - The value of the field  
**inline**(bool) - Whether the field should be displayed inline.

#### `Footer(text=None, icon_url=None)`
Help to create footer dict.

**Parameters**

> **text**(str) - The footer text.  
**icon_url**(str) - The URL of the footer icon. Only HTTP(S) is supported.

#### `Author(name, url=None, icon_url=None)`
Help to create author dict.

**Parameters**
> **name**(str) – The name of the author.  
**url**(str) – The URL for the author.  
**icon_url**(str) – The URL of the author icon. Only HTTP(S) is supported.


## Usage examples
Look in the "UsageExamples" folder.
