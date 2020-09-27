from discord.ext import commands
import discord

from datetime import datetime as dt


class Commands(commands.Cog, name="Commands"):
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
        """Gets how many messages a member has sent"""

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
    async def kontrol_rules(self, ctx):
        """Gets the rules for the user"""
        rls = discord.Embed(title=f"Team Kontrol's Rules", description=f"These are the rules of this server",
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
    async def avatar(self, ctx, member: commands.MemberConverter = None):
        member = member or ctx.member
        user_av = discord.Embed(color=0xffff00, timestamp=dt.utcnow())
        user_av.set_author(name=f"{ctx.author}", icon_url=member.avatar_url)
        user_av.add_field(name="Avatar", value=f"<@{member.id}>", inline=True)
        user_av.set_image(url=member.avatar_url)
        user_av.set_footer(icon_url=ctx.author.avatar_url, text=f"Avatar requested by: {ctx.author}")
        await ctx.send(embed=user_av)

    @commands.command()
    async def python_docs(self, ctx):
        """Gets python docs"""
        await ctx.send("https://docs.python.org/3/")

    @commands.command(aliases=["bot_src"])
    async def source(self, ctx):
        """Gets the source code for the bot"""
        url = "https://github.com/hipika/Pikachu-Discord-Bot"
        await ctx.send(url)

    @commands.command()
    async def github(self, ctx):
        """Pika's github"""
        github = discord.Embed(title="Pika's Github", description="https://github.com/hipika", color=0xffff00)
        await ctx.send(embed=github)

    @commands.command()
    async def info(self, ctx, member: discord.Member = None):
        """Gets the info about a user"""
        member = ctx.author if not member else member
        roles = [role for role in member.roles if role.name != "@everyone"]
        create_date = member.created_at.strftime("%B %#d, %Y, %I:%M:%S %p ")
        join_date = member.joined_at.strftime("%B %#d, %Y, %I:%M:%S %p ")

        info = []
        info.append(f"\n**Registered on**: {create_date}")
        info.append(f"\n**Joined on**: {join_date}")
        info.append(f"\n**Roles[{len(roles)}]**: " + " ".join([role.mention for role in roles]))
        info.append(f"\n**Bot**: {member.bot}")

        user = discord.Embed(title=f"{member.display_name}", color=0xffff00, description=" ".join(info),
                             timestamp=ctx.message.created_at)
        user.set_author(name=f"Info: {member}", icon_url=member.avatar_url)
        user.set_thumbnail(url=member.avatar_url)
        user.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=user)


def setup(bot):
    bot.add_cog(Commands(bot))
