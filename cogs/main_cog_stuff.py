import discord
from discord.ext import commands, tasks
from itertools import cycle

import os

import asyncio

status = cycle(["Playing pika prefix | p.help", "Being a pikachu"])


class MainCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @tasks.loop(seconds=5)
    async def change_status(self):
        await self.client.change_presence(activity=discord.Game(next(status)))



def setup(client):
    client.add_cog(MainCog(client))

