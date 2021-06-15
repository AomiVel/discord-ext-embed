from setuptools import setup
import re


requirements = []
print("requirements.txt file is empty but the package need discord.py more version 2.0.0. This is because now version 2.0.0 is a beta version and I don't wanna force you to update to the Discord.py version 2.0.0 beta.")
"""
with open('requirements.txt', encoding='utf-8') as f:
    requirements = f.read().splitlines()
"""

version = ''
with open('discord/ext/embed/__init__.py', encoding='utf-8') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')


readme = ''
with open('README.md', encoding='utf-8') as f:
    readme = f.read()


packages = [
    'discord.ext.embed'
]

setup(name='discord-ext-embed',
      author='AomiVel',
      url='https://github.com/AomiVel/discord-ext-embeds',
      project_urls={},
      version=version,
      packages=packages,
      license='MIT',
      description="Discord embed's extension",
      long_description=readme,
      long_description_content_type="text/markdown",
      include_package_data=True,
      install_requires=requirements,
      python_requires='>=3.8.0',
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: Japanese',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet'
      ]
)
