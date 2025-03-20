import discord
import random
from discord.ext import commands
import os
import requests
print(os.listdir("Memes"))  
print(os.listdir("Memes-en"))

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

consejos = ["Ahorra energía: Apaga luces y electrodomésticos cuando no los uses.",
    "Usa bombillas LED: Consumen menos electricidad y duran más tiempo.",
    "Reduce el consumo de agua: Cierra el grifo mientras te cepillas los dientes o lavas los platos.",
    "Recicla correctamente: Separa vidrio, plástico, papel y residuos orgánicos.",
    "Reutiliza todo lo posible: Usa botellas reutilizables, bolsas de tela y recipientes de vidrio.",
    "Evita el desperdicio de comida: Compra solo lo necesario y reutiliza sobras en nuevas recetas.",
    "Consume productos locales y de temporada: Reducen la huella de carbono del transporte.",
    "Reduce el consumo de carne: La producción de carne genera emisiones altas de CO₂ y consume mucha agua.",
    "Opta por envases biodegradables: Evita productos con demasiado plástico.",
    "Haz compostaje: Convierte los desechos orgánicos en abono para plantas.",
    "Usa transporte público o comparte coche: Reduce emisiones y ahorra combustible.",
    "Camina o usa bicicleta: Es más ecológico y saludable.",
    "Mantén tu vehículo en buen estado: Un coche bien mantenido consume menos combustible.",
    "Opta por vehículos eléctricos o híbridos: Si es posible, elige opciones con menor impacto ambiental.",
    "Digitaliza documentos: Reduce el uso de papel imprimiendo solo cuando sea necesario.",
    "Desconecta cargadores y dispositivos: Evita el consumo de energía fantasma.",
    "Usa materiales reciclados: Compra cuadernos, bolígrafos y otros artículos ecológicos.",
    "Planta árboles y cuida las áreas verdes: Los árboles ayudan a reducir el CO₂ y mejoran el aire.",
    "Participa en limpiezas comunitarias: Ayuda a recoger basura en parques y playas.",
    "Educa y sensibiliza: Comparte estos consejos con familiares y amigos para fomentar un impacto positivo."
]
    



facts =["Save energy: Turn off lights and appliances when not in use.",
    "Use LED bulbs: They consume less electricity and last longer.",
    "Reduce water consumption: Turn off the tap while brushing your teeth or washing dishes.",
    "Recycle properly: Separate glass, plastic, paper, and organic waste.",
    "Reuse as much as possible: Use reusable bottles, cloth bags, and glass containers.",
    "Avoid food waste: Buy only what is necessary and reuse leftovers in new recipes.",
    "Consume local and seasonal products: They reduce the carbon footprint of transportation.",
    "Reduce meat consumption: Meat production generates high CO₂ emissions and consumes a lot of water.",
    "Opt for biodegradable packaging: Avoid products with excessive plastic.",
    "Compost: Turn organic waste into fertilizer for plants.",
    "Use public transportation or carpool: Reduce emissions and save fuel.",
    "Walk or use a bicycle: It is more eco-friendly and healthier.",
    "Keep your vehicle in good condition: A well-maintained car consumes less fuel.",
    "Choose electric or hybrid vehicles: If possible, opt for lower environmental impact options.",
    "Digitize documents: Reduce paper usage by printing only when necessary.",
    "Unplug chargers and devices: Avoid phantom energy consumption.",
    "Use recycled materials: Buy eco-friendly notebooks, pens, and other supplies.",
    "Plant trees and take care of green areas: Trees help reduce CO₂ and improve air quality.",
    "Participate in community cleanups: Help collect trash in parks and beaches.",
    "Educate and raise awareness: Share these tips with family and friends to encourage a positive impact."
]




@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')
    # Comandos disponibles
    commands_list = '''
    Hi please select your lenguage with the command !english or !spanish
    '''
    channel = bot.get_channel(1331770000083517452)
    await channel.send(commands_list)

@bot.command()
async def spanish(ctx):
    await ctx.send(f'Hola, ¡soy un bot {bot.user}!, puedes utilizar el comando !memes para ver memes para aprender sobre los problemas de el cambio cliamtico y como evitarlo o el comando !consejos para poder ver uno de los 20 consejos al azar, puedes utilizar el comando !github para tener el link para ver el código de este bot, puedes utilizar el comando !version para ver la versión de este bot, ¡gracias!')

@bot.command()
async def english(ctx):
    await ctx.send(f'Hi, I am bot {bot.user}!, you can use the command !ENmemes to see the memes to learn about the problems of the climate change and how not to do it or you can use de command !tips so you can see one of the 20 tips in a random way , you can use the command !github so you can get the link to see this code of this bot, you can use the command !version so you can see the version of this bot, thank you!')

@bot.command()
async def memes(ctx):
    img_name = random.choice(os.listdir("Memes"))
    with open(f'Memes/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def ENmemes(ctx):
    img_name = random.choice(os.listdir("Memes-en"))
    with open(f'Memes/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def consejos(ctx):
    await ctx.send(random.choice(consejos))

@bot.command()
async def facts(ctx):
    await ctx.send(random.choice(facts))

@bot.command()
async def github(ctx):
    await ctx.send(f"https://github.com/ma457775/Miercoles_M2_12Febre.git")

@bot.command()
async def version(ctx):
    await ctx.send(f"1.0")





bot.run("pspdd")
