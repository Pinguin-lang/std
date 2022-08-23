from sys import stdout

def std(sentence: str, ctx) -> None:
  stdout.write(sentence)
  return None

def setup(ctx):
  ctx.mets['std'] = {"python": True, "func": std}
  return ctx
