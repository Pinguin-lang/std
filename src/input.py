from getkey import getkey
from .std import stdout
def inpute(args: list, ctx) -> str:
  stdout.write(args[0]['data'])
  return getkey()

def inputcool(args: list, ctx) -> str:
  stdout.write(args[0]['data'])
  return input()

def setup(ctx):
  ctx.fn['input'] = {"python": True, 'func': inpute, 'args': [{"name": "console", 'type': 'str', 'required': False, 'default': ''}], 'kwargs': []}
  ctx.fn['cinput'] = {"python": True, 'func': inputcool, 'args': [{"name": "console", 'type': 'str', 'required': True, 'default': ''}], 'kwargs': []}
