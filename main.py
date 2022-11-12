import requests 

from discord import app_commands, Intents, Client, Interaction




def check_me(token_test: str) -> dict:
    r = requests.get("https://discord.com/api/v10/users/@me", headers={
        "Yetkilendirme": f"Bot {token_test}"
    })
    
    
    return r.json()
    
    
print("\n".join([
    "Active Developer rozeti alma paneline hoşgeldin.",
    "Lütfen devam etmek için aşağıya botunun tokenini gir:",
    "",
    "Bu uygulamayı yaptıktan sonra pencereyi aktif tutun, davet edip komutu çalıştırdıktan sonra kapatabilirsiniz."
]))



while True:
    token = input("> ")
    data = check_me(token)
    
    
    if data.get("id", None):
        break
        
        
    print("\nGeçersiz bir token girmişsiniz gibi gözüküyor. Tekrar deneyin.")
    
    
class FunnyBadge(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        
        
    async def setup_hook(self) -> None:
        await self.tree.sync(guild=None)
        
        
        
        
client = FunnyBadge(intents=Intents.none())




@client.event
async def on_ready():
    print("\n".join([
        f"~ {client.user} olarak giriş yapıldı. (ID: {client.user.id})",
        "",
        f"~ {client.user} botunu davet etmek için bu linki kullanabilirsiniz:",
        f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&scope=applications.commands%20bot"
    ]))
    

@client.tree.command()
async def merhaba(interaction: Interaction):
    """ Selam verir veya başka bir şeyler der. """
    print(f"> {interaction.user} used the command.")
    await interaction.response.send_message(
        f"Merhaba **{interaction.user}**, bana selam verdiğin için teşekkürler."
    )
    
    
    
client.run(token)
