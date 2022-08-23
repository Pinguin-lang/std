from interpreter import error
def werror(sentence: str, ctx):
  error("No traceback", sentence)

def setup(ctx):
  ctx.mets['error'] = {"python": True, 'func': werror}
  return ctx
