import discord
import os
import pandas as pd
import datetime as dt

# set up gateway intents to pull member info below
intents = discord.Intents.default()
intents.members = True

# create connection to discord
client = discord.Client(intents=intents)


# when logged in *and ready to work*, print message
@client.event
async def on_ready():
    print("Bot is logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.content.lower().startswith('userdate'):
        user_dict = {}
        now = dt.datetime.now().strftime("%d_%m_%Y")
        guild = message.guild
        # print(guild)

        # create generator with all member info
        members = client.get_all_members()
        for member in members:
            if member.guild == guild:
                date = member.joined_at.strftime("%d/%m/%Y %H:%M")
                user_dict[member.name] = date
        # print(user_dict)

        # create dataframe, save it
        df = pd.DataFrame(user_dict.items(), columns=['Username', 'Date Joined']).sort_values("Date Joined")
        print(df)
        df.to_csv(f'{guild} {now} User Joined Dates.csv')

client.run(os.environ['TOKEN'])
