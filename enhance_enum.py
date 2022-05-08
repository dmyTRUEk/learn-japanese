"""
Enhance Enum:
- `@enhance_enum` adds `.get_by_index()` function to Enum class
"""

def enhance_enum(cls):
    assert(cls is not None)
    def get_by_index(index: int):
        assert(isinstance(index, int))
        assert(0 <= index < len(cls))
        return list(cls)[index]
    setattr(cls, "get_by_index", get_by_index)
    return cls

