from urllib.request import urlopen
from typing import Optional, cast


class WebPage:
    def __init__(self, url: str) -> None:
        self.url = url
        self._content: Optional[bytes] = None

    @property
    def content(self) -> bytes:
        if self._content is None:
            print("Retreaving New Page ...")
            with urlopen(self.url) as response:
                self._content = response.read()
        return self._content
