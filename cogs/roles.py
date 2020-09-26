import discord
from discord.ext import commands

import datetime as dt

class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.colors = {
                    "♥️": self.bot.guild.get_role(759245441224409118),  # Red
                    "💙": self.bot.guild.get_role(759245441224409118),  # Blue
                    "💚": self.bot.guild.get_role(759254259626672128),  # Green
                    "🧡": self.bot.guild.get_role(759254299494055996),  # Yellow
            }
            self.reaction_message = await self.bot.get_channel(737184813026508841).fetch_message(759245441224409118)
            self.bot.cogs_ready.read_up("roles")


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if self.bot.ready and payload.message.id == self.reaction_message.id:
            current_roles = filter(lambda r: r in self.colors.keys(), payload.member.roles)
            await payload.member.remove_roles(*current_roles, reason="Role reaction for colors")

            await payload.member.add_roles(self.colors[payload.emoji.name], reason="Role reaction for colors")
            await self.reaction_message.remove_reaction(payload.member, payload.emoji)


    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if self.bot.ready and payload.message.id == self.reaction_message.id:
            member = self.bot.guild.get_member(payload.user_id)
            await member.remove_roles(self.colors[payload.emoji.name], reason="Role reaction for colors")


def setup(bot):
    bot.add_cog(Roles(bot))