import discord
from discord.ext import commands
from scrapers.onlyfans import OnlyFansScraper
from generators.deepfake import DeepfakeGenerator
from security.firewall import DDOSProtection
from utils.blackhat import BlackHatSystem

class C2CBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix="!", intents=intents)
        
        self.scraper = OnlyFansScraper()
        self.deepfake = DeepfakeGenerator()
        self.firewall = DDOSProtection()
        self.blackhat = BlackHatSystem()

        # Load cogs
        self.load_extension("utils.blackhat")
        self.load_extension("scrapers.onlyfans")

    async def on_ready(self):
        print(f"🔥 C2C HEAVEN ONLINE | {self.user.name}")
        await self.blackhat.initialize(self)

bot = C2CBot()
bot.run(os.getenv('DISCORD_TOKEN'))
