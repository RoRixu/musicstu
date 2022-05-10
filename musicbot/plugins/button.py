import discord
from discord.ext import commands
from musicbot import linkutils, utils


class Button(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        sett = utils.guild_to_settings[message.guild]
        button_name = sett.get('button_emote')

        if button_name == "":
            return

        if message.author == self.bot.user:
            return

        host = linkutils.identify_url(message.content)

        guild = message.guild
        emoji = discord.utils.get(guild.emojis, name=button_name)

        if host == linkutils.Sites.YouTube:
            if emoji:
                await message.add_reaction(emoji)

        if host == linkutils.Sites.Spotify:
            if emoji:
                await message.add_reaction(emoji)

        if host == linkutils.Sites.Spotify_Playlist:
            if emoji:
                await message.add_reaction(emoji)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, reaction):
        serv = self.bot.get_guild(reaction.guild_id)

        sett = utils.guild_to_settings[serv]
        button_name = sett.get('button_emote')

        if button_name == "":
            return

        if reaction.emoji.name == button_name:
            channels = serv.text_channels

            for chan in channels:
                if chan.id == reaction.channel_id:
                    if reaction.member == self.bot.user:
                        return

                    try:
                        if reaction.member.voice.channel == None:
                            return
                    except:
                        message = await chan.fetch_message(reaction.message_id)
                        await message.remove_reaction(reaction.emoji, reaction.member)
                        return
                    message = await chan.fetch_message(reaction.message_id)
                    await message.remove_reaction(reaction.emoji, reaction.member)

            current_guild = utils.get_guild(self.bot, message)
            audiocontroller = utils.guild_to_audiocontroller[current_guild]

            url = linkutils.get_url(message.content)

            host = linkutils.identify_url(url)

            if host == linkutils.Sites.Spotify:
                await audiocontroller.process_song(url)

            if host == linkutils.Sites.Spotify.Spotify_Playlist:
                await audiocontroller.process_song(url)

            if host == linkutils.Sites.YouTube:
                await audiocontroller.process_song(url)

        if reaction.emoji.name == "⏯":
            channels = serv.text_channels

            for chan in channels:
                if chan.id == reaction.channel_id:
                    if reaction.member == self.bot.user:
                        return

                    try:
                        if reaction.member.voice.channel == None:
                            return
                    except:
                        message = await chan.fetch_message(reaction.message_id)
                        await message.remove_reaction(reaction.emoji, reaction.member)
                        return
                    message = await chan.fetch_message(reaction.message_id)
                    await message.remove_reaction(reaction.emoji, reaction.member)

            current_guild = utils.get_guild(self.bot, message)
            if current_guild is None:
                await ctx.send(config.NO_GUILD_MESSAGE)
                return
            if current_guild.voice_client is None:
                return
            if current_guild.voice_client.is_playing():
                print("should pause")
                current_guild.voice_client.pause()
                return
            else:
                current_guild.voice_client.resume()
                return

        if reaction.emoji.name ==  "⏭":
            channels = serv.text_channels

            for chan in channels:
                if chan.id == reaction.channel_id:
                    if reaction.member == self.bot.user:
                        return

                    try:
                        if reaction.member.voice.channel == None:
                            return
                    except:
                        message = await chan.fetch_message(reaction.message_id)
                        await message.remove_reaction(reaction.emoji, reaction.member)
                        return
                    message = await chan.fetch_message(reaction.message_id)
                    await message.remove_reaction(reaction.emoji, reaction.member)

            current_guild = utils.get_guild(self.bot, message)
            current_guild.voice_client.stop()

        if reaction.emoji.name ==  "⏮":
            channels = serv.text_channels

            for chan in channels:
                if chan.id == reaction.channel_id:
                    if reaction.member == self.bot.user:
                        return

                    try:
                        if reaction.member.voice.channel == None:
                            return
                    except:
                        message = await chan.fetch_message(reaction.message_id)
                        await message.remove_reaction(reaction.emoji, reaction.member)
                        return
                    message = await chan.fetch_message(reaction.message_id)
                    await message.remove_reaction(reaction.emoji, reaction.member)

            current_guild = utils.get_guild(self.bot, message)
            audiocontroller = utils.guild_to_audiocontroller[current_guild]
            audiocontroller.playlist.loop = False

            audiocontroller.timer.cancel()
            audiocontroller.timer = utils.Timer(audiocontroller.timeout_handler)

            if current_guild is None:
                return
            await utils.guild_to_audiocontroller[current_guild].prev_song()

        if reaction.emoji.name ==  "⏹":
            channels = serv.text_channels

            for chan in channels:
                if chan.id == reaction.channel_id:
                    if reaction.member == self.bot.user:
                        return

                    try:
                        if reaction.member.voice.channel == None:
                            return
                    except:
                        message = await chan.fetch_message(reaction.message_id)
                        await message.remove_reaction(reaction.emoji, reaction.member)
                        return
                    message = await chan.fetch_message(reaction.message_id)
                    await message.remove_reaction(reaction.emoji, reaction.member)

            current_guild = utils.get_guild(self.bot, message)

            audiocontroller = utils.guild_to_audiocontroller[current_guild]
            audiocontroller.playlist.loop = False
            if current_guild is None:
                return
            await utils.guild_to_audiocontroller[current_guild].stop_player()

        if reaction.emoji.name ==  "🔉":
            channels = serv.text_channels

            for chan in channels:
                if chan.id == reaction.channel_id:
                    if reaction.member == self.bot.user:
                        return

                    try:
                        if reaction.member.voice.channel == None:
                            return
                    except:
                        message = await chan.fetch_message(reaction.message_id)
                        await message.remove_reaction(reaction.emoji, reaction.member)
                        return
                    message = await chan.fetch_message(reaction.message_id)
                    await message.remove_reaction(reaction.emoji, reaction.member)

            current_guild = utils.get_guild(self.bot, message)
            currentVolume = utils.guild_to_audiocontroller[current_guild].volume
            if (currentVolume - 10) < 0:
                utils.guild_to_audiocontroller[current_guild].volume = 0
            else:
                utils.guild_to_audiocontroller[current_guild].volume = currentVolume - 10

        if reaction.emoji.name ==  "🔊":
            channels = serv.text_channels

            for chan in channels:
                if chan.id == reaction.channel_id:
                    if reaction.member == self.bot.user:
                        return

                    try:
                        if reaction.member.voice.channel == None:
                            return
                    except:
                        message = await chan.fetch_message(reaction.message_id)
                        await message.remove_reaction(reaction.emoji, reaction.member)
                        return
                    message = await chan.fetch_message(reaction.message_id)
                    await message.remove_reaction(reaction.emoji, reaction.member)

            current_guild = utils.get_guild(self.bot, message)
            currentVolume = utils.guild_to_audiocontroller[current_guild].volume
            if (currentVolume +10) > 100:
                utils.guild_to_audiocontroller[current_guild].volume = 100
            else:
                utils.guild_to_audiocontroller[current_guild].volume = currentVolume + 10

def setup(bot):
    bot.add_cog(Button(bot))
