"""
Example slash commands
"""
import disspy
from disspy import app_commands, StrOption, IntOption

client = disspy.Client(token="TOKEN")  # Create client


# Example command without options
@client.command()
@app_commands.describe("Test")
async def hello(ctx: disspy.Context):
    a = ""
    with open("hello.txt", "r", encoding="utf-8") as f:
        a = f.read()

    await ctx.respond(str(a))


# Example command with options
@client.command()
@app_commands.describe("Example command")
@app_commands.options.describe(message=StrOption().description("Message").required(),
                               integer=IntOption().description("Integer for math operation"))
async def foo(ctx: disspy.Context, message: str, integer: int = None):
    if integer:
        await ctx.respond(message, integer + 2, sep=" | ")
    else:
        await ctx.respond(message)


# Example context menus
# Message context menu
@client.context_menu()
async def info(ctx: disspy.Context, message: disspy.Message):
    await ctx.respond(f"Content: {message.content}", f"Channel id: {message.channel.id}", f"Id: {message.id}")


# User context menu
@client.context_menu()
async def fullname(ctx: disspy.Context, user: disspy.User):
    await ctx.respond(user.fullname)

client.run()  # Running bot