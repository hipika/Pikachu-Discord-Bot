from discord.ext import commands
import discord

from datetime import datetime as dt


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx, *, message):
        """Make a poll for a suggestion"""
        await ctx.message.delete()
        embd = discord.Embed(description=f"{message}", timestamp=dt.utcnow())
        embd.set_author(name=f"Poll created by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        # embd.set_thumbnail(url=self.bot.author.avatar_url)
        msg = await ctx.channel.send(embed=embd)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")

    @commands.command(aliases=["msg", "msgs"])
    async def messages(self, ctx, member: discord.Member = None):
        """Gets how many messgages a member has sent"""

        member = ctx.author if member is None else member

        channel = ctx.channel

        msg_count = 0

        async for msg in channel.history(limit=None):
            if msg.author == member:
                msg_count += 1
        await ctx.send(f"{member.display_name} has sent:\n"
                       f"{msg_count} messages.")

    @commands.command()
    async def rules(self, ctx):
        """Gets the rules for the user"""
        rls = discord.Embed(title=f"Pika's Cave Rules", description=f"These are the rules of this server",
                            color=0xffff00)
        rls.add_field(name="1.", value=f"**No Racism/Hate Speech.**", inline=True)
        rls.add_field(name="2.", value=f"**Do not send Malicious Content.**", inline=True)
        rls.add_field(name="3.", value=f"**Always talk in English.**", inline=True)
        rls.add_field(name="4.", value=f"**No NSFW in any of the chats.**", inline=True)
        rls.add_field(name="5.", value=f"**No spreading/leaking Personal Information.**", inline=True)
        rls.add_field(name="6.", value=f"**Only self promote in the self promotion channel.**", inline=True)
        rls.add_field(name="7.", value=f"**Please respect the Discord TOS.**", inline=True)
        rls.add_field(name="8.", value=f"**Please only talk in the respective channels.**", inline=True)
        rls.add_field(name="9.", value=f"**Read all the rules above.**", inline=True)
        rls.set_footer(icon_url=ctx.author.avatar_url, text=f"Rules requested by: {ctx.author}")

        await ctx.send(embed=rls)

    @commands.command()
    async def member_count(self, ctx):
        """Gets the member count"""
        members = discord.Embed(title="Member count", color=0xffff00)
        members.add_field(name="Members: ", value=f"There are {ctx.guild.member_count} members", inline=True)
        await ctx.send(embed=members)

    @commands.command(aliases=["av"])
    async def avatar(self, ctx, member: discord.Member):
        # roles = [role for role in member.roles if role.name != "@everyone"]
        # avatar_url = ctx.author.avatar_url
        member = member or ctx.member
        user_av = discord.Embed(color=0xffff00, timestamp=dt.utcnow())
        user_av.set_author(name=f"{ctx.author}", icon_url=member.avatar_url)
        user_av.add_field(name="Avatar", value=f"<@{member.id}>", inline=True)
        user_av.set_image(url=member.avatar_url)
        user_av.set_footer(icon_url=ctx.author.avatar_url, text=f"Avatar requested by: {ctx.author}")
        await ctx.send(embed=user_av)


def setup(bot):
    bot.add_cog(Commands(bot))
