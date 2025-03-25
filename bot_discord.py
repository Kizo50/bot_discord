import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

# Crear el bot y pues el ! es el prefijo para poder usarlo
bot = commands.Bot(command_prefix="!", intents=intents)

#LISTA DE COMANDOS

command_list = {
    "comandos": "Muestra información sobre la lista de comandos.",
    "info": "Muestra información sobre el creador del bot.",
    "kebap": "Muestra como craftear el item de kebap.",
    "aceitegirasol": "Muestra como craftear el item de aceite de girasol.",
    "patatasfritas": "Muestra como craftear el item patatas fritas.",
    "botesalsayogurt": "Muestra como craftear el item bote salsa de yogurt.",
    "espadakebap": "Muestra como craftear el item espada kebap.",
    "hamburguesa": "Muestra como craftear el item hamburguesa.",
    "picokebap": "Muestra como craftear el item picokebap.",
    "azadakebap": "Muestra como craftear el item azadakebap.",
    "palakebap": "Muestra como craftear el item palakebap.",
    "hachakebap": "Muestra como craftear el item hachakebap.",
    "paella": "Muestra como craftear el item de paella.",
    "churros": "Muestra como craftear el item de churros.",
    "panpita": "Muestra como craftear el item de pan pita.",
    "tortilla": "Muestra como craftear el item de tortilla.",
    "logo": "Muestra el logo.",
    "clear": "Borra todas las sentencias anteriores."
}


# Comandos sobre el mod minecraft
@bot.command()
async def info(ctx):
    await ctx.send(
        "Soy un bot creado por Kizo50. \n Aquí puedes realizar consultas para saber como craftear los items. "
    )


@bot.command()
async def kebap(ctx):
    await ctx.send(
        "Items que necesitas para hacer un kebap: 1)Pan 2)Bote salsa de yogurt 3)Pollo"
    )
    # Adjuntar la imagen
    file = discord.File("crafteo_kebap.png", filename="crafteo_kebap.png")
    await ctx.send(file=file)


@bot.command()
async def aceitegirasol(ctx):
    await ctx.send(
        "Items que necesitas para hacer aceite de girasol: 1) Tres girasoles 2)Frasco de Cristal"
    )
    file = discord.File("crafteo_aceitegirasol.png",
                        filename="crafteo_aceitegirasol.png")
    await ctx.send(file=file)


@bot.command()
async def patatasfritas(ctx):
    await ctx.send(
        "Items que necesitas para hacer patatas fritas: 1)Aceite de girasol 2)Patata "
    )
    file = discord.File("crafteo_patatasfritas.png",
                        filename="crafteo_patatasfritas.png")
    await ctx.send(file=file)


@bot.command()
async def botesalsayogurt(ctx):
    await ctx.send(
        "Items que necesitas para hacer bote de salsa de yogurt: 1)Salsa de yogurt 2)Frasco de Cristal"
    )
    file = discord.File("crafteo_botesalsayogurt.png",
                        filename="crafteo_botesalsayogurt.png")
    await ctx.send(file=file)


@bot.command()
async def espadakebap(ctx):
    await ctx.send(
        "Items que necesitas para hacer una espada de kebap: 1)Dos Kebaps 2)Palo"
    )
    file = discord.File("crafteo_espada_kebap.png",
                        filename="crafteo_espada_kebap.png")
    await ctx.send(file=file)


@bot.command()
async def hamburguesa(ctx):
    await ctx.send(
        "Items que necesitas para hacer una hamburguesa: 1)Pan 2)Huevo 3)Filete Asado"
    )
    file = discord.File("crafteo_hamburguesa.png",
                        filename="crafteo_hamburguesa.png")
    await ctx.send(file=file)


@bot.command()
async def picokebap(ctx):
    await ctx.send(
        "Items que necesitas para hacer una hamburguesa: 1)Tres kebaps 2)Palo")
    file = discord.File("crafteo_picokebap.png",
                        filename="crafteo_picokebap.png")
    await ctx.send(file=file)


@bot.command()
async def palakebap(ctx):
    await ctx.send(
        "Items que necesitas para hacer una pala: 1)Un kebap 2)Dos palos")
    file = discord.File("pala_fotokebap.png", filename="pala_fotokebap.png")
    await ctx.send(file=file)


@bot.command()
async def hachakebap(ctx):
    await ctx.send(
        "Items que necesitas para hacer una hacha: 1)Tres kebaps 2)Dos palos")
    file = discord.File("hacha_fotokebap.png", filename="hacha_fotokebap.png")
    await ctx.send(file=file)


@bot.command()
async def azadakebap(ctx):
    await ctx.send(
        "Items que necesitas para hacer una azada: 1)Dos kebaps 2)Dos palos")
    file = discord.File("crafteo_azada_kebap.png",
                        filename="crafteo_azada_kebap.png")
    await ctx.send(file=file)


@bot.command()
async def paella(ctx):
    await ctx.send(
        "Items que necesitas para hacer una azada: 1)Un pollo cocinado 2)Un conejo cocinado 3)Un bacalado cocinado 4)Un cuenco "
    )
    file = discord.File("paella_minecraft.png",
                        filename="paella_minecraft.png")
    await ctx.send(file=file)


@bot.command()
async def churros(ctx):
    await ctx.send(
        "Items que necesitas para hacer una azada: 1)Un huevo 2)Un item trigo 3)Un cubo de leche "
    )
    file = discord.File("churros_minecraft.png",
                        filename="churros_minecraft.png")
    await ctx.send(file=file)


@bot.command()
async def panpita(ctx):
    await ctx.send("Items que necesitas para hacer una azada: 1)Dos de trigo ")
    file = discord.File("pandepita_minecraft.png",
                        filename="pandepita_minecraft.png")
    await ctx.send(file=file)


@bot.command()
async def tortilla(ctx):
    await ctx.send("Items que necesitas para hacer una azada: 1)Un huevo 2)Una patata ")
    file = discord.File("tortilla_minecraft.png",
                        filename="tortilla_minecraft.png")
    await ctx.send(file=file)


@bot.command()
async def logo(ctx):
    await ctx.send("Te adjunto la foto del logo del mod de minecraft")
    file = discord.File("logo_mod_minecraft.png",
                        filename="logo_mod_minecraft.png")
    await ctx.send(file=file)


@bot.command()
async def comandos(ctx):
    comandos_msg = "**Lista de comandos disponibles:**\n"
    for cmd, desc in command_list.items():
        comandos_msg += f"`!{cmd}`: {desc}\n"
    await ctx.send(comandos_msg)


@bot.command()
async def clear(ctx, amount: int = 100):
    """
    Borra mensajes en un canal de texto del servidor.
    """
    # Verifica si el comando se ejecuta en un servidor
    if isinstance(ctx.channel, discord.DMChannel):
        await ctx.send(
            "Este comando no se puede usar en mensajes directos, solo en canales de texto privado."
        )
        return

    # Elimina los mensajes en el canal actual
    # Delete after el tiempo que tarda en borrar los mensajes
    deleted = await ctx.channel.purge(limit=amount)
    await ctx.send(f"Se han borrado {len(deleted)} mensajes.", delete_after=3)


# Evento para confirmar que el bot esta listo
@bot.event
async def on_ready():
    print(f"{bot.user} está en línea y listo para responder.")


bot.run(os.environ['token'])
