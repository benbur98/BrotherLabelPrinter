from brother_label_printer_control.constants import Media
from brother_label_printer_control.labels.box import Box
from brother_label_printer_control.labels.label import Label
from brother_label_printer_control.labels.text import Padding, Text
from pydantic import BaseModel, Field, field_validator

from ..settings import get_settings


class PrintRequest(BaseModel):
    text: str
    height: int
    padding: Padding = Field(default_factory=lambda: Padding(top=0, right=0, bottom=0, left=0))
    font: str = Field(default_factory=lambda: get_settings().font)
    media: Media = Field(default_factory=lambda: get_settings().media)

    @field_validator("padding", mode="before")
    def set_padding(cls, padding: dict[str, int] | Padding) -> Padding:
        if isinstance(padding, dict):
            return Padding.from_dict(padding)
        return padding

    @field_validator("media", mode="before")
    def set_media(cls, media: str | Media) -> Media:
        if isinstance(media, str):
            return Media.get(media)
        return media

    def generate_label(self, media: Media) -> Label:
        height = min(media.value.printarea, self.height)  # Cap the Height to the media's printarea

        text = Text(height, self.text, font_path=self.font, padding=self.padding)

        box = Box(media.value.printarea, text)

        return Label(box)
