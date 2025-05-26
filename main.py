import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True  # メンバー参加イベントを受け取るために必要
intents.guilds = True

bot = commands.Bot(command_prefix="welc.", intents=intents)

WELCOME_CHANNEL_ID = 1375077085529243678  # 送信先チャンネルのIDに置き換えてください
WELCOME_IMAGE_URL = "https://cdn.glitch.global/d1022a5c-ecf8-42dd-96b3-1b0094a64966/standard.gif?v=1748236168821"  # 画像URLに置き換えてください

@bot.event
async def on_member_join(member: discord.Member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            title=f"Welcome to {member.guild.name}!",
            description=f"Thank you for joining {member.mention}",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=member.avatar.url)  # ★ ユーザーのアイコンをサムネイルに
        embed.set_image(url=WELCOME_IMAGE_URL)
        await channel.send(embed=embed)

@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.watching, name="𝑭𝒓𝒆𝒂𝒌'𝒔 𝑺𝒆𝒓𝒗𝒆𝒓")
    await bot.change_presence(activity=activity)
    print(f'Logged in as {bot.user}')

DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
if DISCORD_TOKEN is None:
    print("DISCORD_BOT_TOKEN が設定されていません。")
else:
    print("Botが正常に起動しました。")

keep_alive()
bot.run(DISCORD_TOKEN)
