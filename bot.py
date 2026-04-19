import discord,requests,json,os
from dotenv import load_dotenv

def get_meme():
    response=requests.get(f'https://meme-api.com/gimme/wholesomememes')
    json_data=json.loads(response.text)
    return json_data['url']


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    
    async def on_message(self,message):
        if message.author == self.user:
            return
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content=True

load_dotenv()
token= os.getenv('DISCORD_TOKEN')

client = MyClient(intents=intents)
client.run(token)