# ---- ALl of the modules ----

import discord
import json
from discord.ext import commands
from discord.ext.commands import CommandNotFound, MissingPermissions, MissingRole, MissingRequiredArgument
from itertools import cycle

from config import Config
import os
import asyncio
import datetime as dt
import logging

class Pika(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix=kwargs.pop('command_prefix', ('p.', 'P.', 'pika.', 'Pika.')),
                         case_insensitive=True,
                         **kwargs)

    async def on_ready(self):
        await self.change_presence(status=discord.Status.idle, activity=discord.Game("pika prefix | p.help"))

        # loads all the cods in the cog folder
        for filename in os.listdir("cogs"):
            if filename.endswith(".py"):
                self.load_extension(f"cogs.{filename[:-3]}")

        print("Bot is online")

    async def on_member_join(self, member):
        """New member joined"""
        channel = self.get_channel(747873288365277377)
        await channel.send(f"{member.mention} has joined the server.")

    async def on_member_remove(self, member):
        """Member left"""
        channel = self.get_channel(747873401095585902)
        await channel.send(f"{member.mention} why did you leave? Please rejoin, we are glad to have you!")

    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            await ctx.send("Command not found!")
        elif isinstance(error, MissingPermissions):
            await ctx.send("You are missing the permission(s) to use that command.")
        elif isinstance(error, MissingRole):
            await ctx.send("You are missing the role(s) to use that command.")
        elif isinstance(error, MissingRequiredArgument):
            await ctx.send("You are missing a required argument.")
        else:
            raise error

    @staticmethod
    async def is_it_me(ctx):
        return ctx.author.id == 681605894152519697

    # @bot.command()
    # @commands.has_permissions(manage_messages=True)
    # async def clear(ctx, amount=10):
    #     await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.check(is_it_me)
    async def author(self, ctx):
        await ctx.send(f"Hi I am the author: {ctx.author} of this bot.")

    async def setup(self, **kwargs):
        try:
            await self.start(Config.TOKEN, **kwargs)
        except KeyboardInterrupt:
            await self.close()

bot = Pika()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.setup())

# @bot.command()
# async def kick(ctx, member: discord.Member, *, reason=None):
#     amount = 2
#     await member.kick(reason=reason)
#     await ctx.send(f"{member.mention} has been kicked!")
#     await ctx.channel.purge(limit=amount)
#
#
# @bot.command()
# async def ban(ctx, member: discord.Member, *, reason=None):
#     amount = 2
#     await member.ban(reason=reason)
#     await ctx.send(f"Banned {member.mention}")
#     await ctx.channel.purge(limit=amount)
#
#
# @bot.command()
# async def unban(ctx, *, member):
#     banned_users = await ctx.guild.bans()
#     member_name, member_discriminator = member.split("#")
#
#     for ban_entry in banned_users:
#         user = ban_entry.users
#
#         if (user.name, user.discriminator) == (member_name, member_discriminator):
#             await ctx.guild.unban(user)
#             await ctx.send(f"You have been unbanned {user.mention}")


# @bot.command()
# async def poll(ctx, *, message):
#     """Make a poll for a suggestion"""
#     await ctx.message.delete()
#     embd = discord.Embed(description=f"{message}")
#     embd.set_author(name=f"Poll created by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
#     msg = await ctx.channel.send(embed=embd)
#     await msg.add_reaction("👍")
#     await msg.add_reaction("👎")
