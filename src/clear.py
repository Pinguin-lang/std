from os import system, name

def clear(args: list, ctx):
  if name == 'nt':
    system('cls')
  else:
    system('clear')

def setup(ctx):
  ctx.fn['clear'] = {"python": True, 'func': clear, 'args': [], 'kwargs': []}
  return ctx
