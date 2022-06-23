import toml
from pathlib import Path

pyproject = Path('__file__').parents[0].joinpath('pyproject.toml').resolve()

__version__ = toml.load(pyproject)['tool']['poetry']['version']
