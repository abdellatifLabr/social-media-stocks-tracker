from importlib import import_module


def get_prodvider(name, *args, **kwargs):
  provider_module = import_module(f'{__name__}.{name}')
  return provider_module.run(*args, **kwargs)
