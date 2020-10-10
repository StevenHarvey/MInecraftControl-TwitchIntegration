from twitchio.ext import commands
import deffuc
# api token can be passed as test if not needed.
# Channels is the initial channels to join, this could be a list, tuple or callable
bot = commands.Bot(
    irc_token='IRC TOKEN',
    api_token='API TOKEN',
    nick='NICK',
    prefix='!',
    initial_channels=['CHANNEL']
)


# Register an event with the bot
@bot.event
async def event_ready():
    print(f'Ready | {bot.nick}')


@bot.event
async def event_message(message):
    print(message.content)

    # If you override event_message you will need to handle_commands for commands to work.
    await bot.handle_commands(message)


# Register a command with the bot
@bot.command(name='forward', aliases=['t'])
async def forward(ctx):
    await ctx.send('Walking forward for 5 seconds')
    deffuc.forward()


@bot.command(name='left', aliases=['t'])
async def left(ctx):
    await ctx.send('Walking left for 2 seconds')
    deffuc.left()


@bot.command(name='right', aliases=['t'])
async def right(ctx):
    await ctx.send('Walking right for 2 seconds')
    deffuc.right()


@bot.command(name='back', aliases=['t'])
async def back(ctx):
    await ctx.send('Walking forward for 5 seconds')
    deffuc.back()


@bot.command(name='inv', aliases=['t'])
async def inv(ctx, foo, argu1=None):
    print(foo)
    if "active" not in deffuc.target or foo == "tog":
        if "tog" not in foo:
            await ctx.send('Fixing inventory')
            deffuc.inventory(foo, argu1)
        else:
            await ctx.send('Toggling inventory')
            deffuc.inventory(foo, argu1)
    else:
        await ctx.send("Please close inventory first(!inv tog)")


@bot.command(name='help', aliases=['t'])
async def help(ctx, foo, argu1=None):
    print('foo')
bot.run()
