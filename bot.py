from get_page import get_page
from courses_list import make_list
import discord
from discord import app_commands
from dotenv import load_dotenv
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
intents.message_content = True


@client.event
async def on_ready():
    await tree.sync()
    print(f'Logged in as {client.user.name} ({client.user.id})')
    print('-' * 48)


@tree.command(name='강좌', description='모든 강좌를 보여줍니다')
async def course_list(interaction: discord.Interaction):
    await interaction.response.defer()

    response = get_page()
    courses = make_list(response.text)

    embeds = []

    for course in courses:
        title = course['course_title']
        name = course['professor']
        link = course['course_link']
        image = course['image_src']

        embed=discord.Embed(title="", url="", description=name, color=0xffffff)
        embed.set_author(name=title, url=link, icon_url=image)
        embed.set_thumbnail(url=image)

        embeds.append(embed)

    await interaction.followup.send(content='', embeds=embeds)

load_dotenv("token.env")
token = os.environ.get("token")
client.run(token)
