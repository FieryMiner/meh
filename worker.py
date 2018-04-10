    import discord
    import asyncio

    client = discord.Client()

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    @client.event
    async def on_message(message):
        if message.content == "Hello":
            await client.send_message(message.channel, "World")

    client.run(<NDMyNDcxNTQ5NTE0MjE5NTIw.Da5TJw.SyxABm46No4S_20diXBh7bygVxE>)