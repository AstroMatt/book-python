"""
>>> assert type(result) is frozenset
>>> assert 'a' in result
>>> assert 1 in result
>>> assert 2.2 in result
"""

result = frozenset({'a', 1, 2.2})
