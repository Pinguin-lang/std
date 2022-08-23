from interpreter import error
def werror(sentence: str, ctx):
  error("No traceback", sentence)

def warning(sentence: str, ctx):
  print(f'\033[31mCode raised a warning\n {sentence}\033[00m')

def setup(ctx):
  ctx.mets['error'] = {"python": True, 'func': werror}
  ctx.mets['warning'] = {"python": True, 'func': warning}
  return ctx
