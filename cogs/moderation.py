import discord
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument

import datetime
import logging

class Moderation(commands.Cog):
    def __init__(self, bot):
        @commands.command()
        @commands.guild_only()
        @commands.has_permissions(kick_members=True)
        async def kick(self, ctx, member: discord.Member, *, reason=None):
            """Kicks the member"""
            await ctx.guild.kick(user=member, reason=reason)

            embd = discord.Embed(title=f"{ctx.author.name} has kicked: {member.name}", description=reason,
                                 color=0xffff00)
            await ctx.send(embed=embd)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Bans the member"""
        await ctx.guild.ban(user=member, reason=reason)
        embd = discord.Embed(title=f"{ctx.author.name} has banned: {member.name}", description=reason, color=0xffff00)
        await ctx.send(embed=embd)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"""Please specify a member to ban:
                    For example: **p.ban @MemberNoob**""")


    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member, *, reason=None):
        """Unbans the member"""
        member = await self.bot.fetch_user(int(member))

        await ctx.guild.unban(member, reason=reason)
        embd = discord.Embed(title=f"{ctx.author.name} has unbanned: {member.name}", description=reason, color=0xffff00)
        await ctx.send(embed=embd)

    @commands.command(aliases=["purge"])
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        """Mutes the member"""
        role = discord.utils.get(member.guild.roles, name="Muted")
        # cannot_mute = discord.utils.get(member.guild.roles, name="Moderator")
        # no_mute = discord.utils.get(member.guild.roles, name="Helper")
        #
        # if no_mute.id != cannot_mute.id:
        #     embd_1 = discord.Embed(title=f"That role is a mod/admin, I cannot mute that role.")
        #     await ctx.send(embed=embd_1)

        await member.add_roles(role)
        embd = discord.Embed(title=f"{ctx.author.name} has muted: {member.display_name}", description=reason,
                             color=0xffff00)
        embd.set_author(name=f"{ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embd)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member, *, reason=None):
        """Unmutes the member"""
        role = discord.utils.get(member.guild.roles, name="Muted")
        # await ctx.guild.unmute(user=member, reason=reason)
        await member.remove_roles(role)

        embd = discord.Embed(title=f"{ctx.author.name} has unmuted: {member.display_name}", description=reason,
                             color=0xffff00)

        await ctx.send(embed=embd)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount)


def setup(bot):
    bot.add_cog(Moderation(bot))
