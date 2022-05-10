import datetime

import discord
from config import config

class Song():
    def __init__(self, origin, host, base_url=None, uploader=None, uploader_url = None, title=None, duration=None, webpage_url=None, thumbnail=None,requester=None,channel=None):
        self.host = host
        self.origin = origin
        self.base_url = base_url
        self.info = self.Sinfo(uploader, uploader_url, title, duration,
                               webpage_url, thumbnail,requester,channel)


    class Sinfo:
        def __init__(self, uploader, uploader_url, title, duration, webpage_url, thumbnail,requester,channel):
            self.uploader = uploader
            self.uploader_url = uploader_url
            self.title = title
            self.duration = duration
            self.webpage_url = webpage_url
            self.thumbnail = thumbnail
            self.output = ""
            self.requester = requester
            self.channel = channel

        def format_output(self, playtype):

            embed = discord.Embed(title=playtype, description='```\n{0.title}\n```'.format(self), color=config.EMBED_COLOR)

            if self.duration is not None:
                embed.add_field(name=config.SONGINFO_DURATION,
                                value="{}".format(self.duration))
            else:
                embed.add_field(name=config.SONGINFO_DURATION,
                                value=config.SONGINFO_UNKNOWN_DURATION)
            embed.add_field(name='Requested by', value=self.requester.mention)
            embed.add_field(name='Uploader', value='[{0.uploader}]({0.uploader_url})'.format(self))
            embed.add_field(name='URL', value='[Click]({0.webpage_url})'.format(self))

            if self.thumbnail is not None:
                embed.set_thumbnail(url=self.thumbnail)

            return embed

