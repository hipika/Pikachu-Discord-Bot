import discord
from discord.ext import commands

import googletrans
from googletrans import Translator

import datetime as dt


class Translate(commands.Cog, name="Commands"):
    def __init__(self, bot):
        self.bot = bot
        self.translator = Translator()

    @commands.command(aliases=["ts"])
    async def translate(self, ctx, *, text):
        """Translates whatever input you put into English"""
        output = self.translator.translate(str(text), src="auto", dest="en").text
        embed = discord.Embed()
        embed.add_field(name="Translated", value=f"{output}", inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Translate(bot))
