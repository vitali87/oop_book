import re
from pathlib import Path

from src.zip_processor import ZipProcessor


class TextTweaker(ZipProcessor):
    def __init__(self, archive: Path) -> None:
        super().__init__(archive)
        self.find: str
        self.replace: str

    def find_and_replace(
            self,
            find: str,
            replace: str
    ) -> "TextTweaker":
        self.find = find
        self.replace = replace
        return self

    def transform(self, extracted: Path) -> None:
        input_text = extracted.read_text()
        output_text = re.sub(
            self.find,
            self.replace,
            input_text
        )
        extracted.write_text(output_text)
