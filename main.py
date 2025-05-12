# Installer les dépendances nécessaires
# Pour commencer le raid : (?startraid)
# Pour arrêter le raid : (?unraid)
# Pour mettre le raid en pause : (?pause)
# Pour reprendre le raid : (?resume)
# Ouvrir le terminal et exécuter les commandes :
# python.exe -m pip install --upgrade pip
# pip install nextcord
# pip install discord.py


import nextcord
from nextcord.ext import commands
import os

# Activer les intents nécessaires
intents = nextcord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True

# Variable de contrôle pour mettre en pause le raid
raid_paused = False

# Création du bot avec intents
bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} est prêt.')

# Commande pour configurer le raid (créer des salons)
@bot.command()
async def startraid(ctx):
    global raid_paused
    if raid_paused:  # Si le raid est en pause, ne pas créer de salons
        await ctx.send("Le raid est actuellement en pause.")
        return

    guild = ctx.guild  # Accès au serveur
    if guild is None:
        await ctx.send("Je ne peux pas créer de salons ici.")
        return

    #  créer un nombre infini de salons(tu peux ajuster ce nombre si nécessaire)
    for _ in range(9999999999999999999999999999999999999999): 
        if raid_paused:  # Vérifie l'état de la pause avant chaque création de salon
            await ctx.send("Le raid a été mis en pause.")
            return

        channel = await guild.create_text_channel(name='⛔⛔⛔⛔⛔⛔⛔⛔⛔')  # Création du salon
        await channel.send("@everyone stupide https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSb0QZ5oBICb6nkBN-sVnbproi9Z2THCeQrMw&s")  # Envoi du message

# Commande pour supprimer les salons créés par le raid
@bot.command()
async def unraid(ctx):
    guild = ctx.guild
    if guild is None:
        await ctx.send("Je ne peux pas nettoyer les salons ici.")
        return

    deleted_count = 0
    for channel in guild.text_channels:
        if channel.name.startswith("raid-par-actarix"):  # Vérifie si le nom commence par "raid-par-actarix"
            await channel.delete()
            deleted_count += 1
    await ctx.send(f"🧹 {deleted_count} salons supprimés.")  # Envoie un message après suppression

# Commande pour mettre en pause le raid
@bot.command()
async def pause(ctx):
    global raid_paused
    raid_paused = True
    await ctx.send("Le raid a été mis en pause.")

# Commande pour reprendre le raid
@bot.command()
async def resume(ctx):
    global raid_paused
    raid_paused = False
    await ctx.send("Le raid a repris.")

# Remplacez "YOUR_TOKEN" par votre token Discord
bot.run("YOUR_TOKEN")
