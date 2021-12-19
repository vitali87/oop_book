from typing import Optional


class LongNameDict(dict[str,int]):
    def longest_key(self) -> Optional[str]:
        """In effect, max(self, key = len), but less obscure"""
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key
        return longest