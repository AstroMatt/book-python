"""
>>> isinstance(result, Path)
True
>>> current_directory = Path.cwd()
>>> str(current_directory) in str(result)
True
"""

from pathlib import Path


filename = input('Type filename: ')
result = Path(Path.cwd(), filename)
