from pathlib import Path

from PIL import Image

from src.zip_processor import ZipProcessor


class ImgTweaker(ZipProcessor):
    def transform(self, extracted: Path) -> None:
        image = Image.open(extracted)
        scaled = image.resize(size=(640, 960))
        scaled.save(extracted)
