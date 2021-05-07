import os
from importlib import import_module


def get_providers():
    for provider_file in os.listdir(os.path.dirname(os.path.abspath(__file__))):
        if provider_file[0] != '$':
            continue

        provider = provider_file.replace('.py', '')
        yield import_module(f'{__package__}.{provider}')


def get_prodvider(name, *args, **kwargs):
    provider_module = import_module(f'{__name__}.${name}')
    return provider_module.run(*args, **kwargs)
