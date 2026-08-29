from functools import lru_cache

from brother_label_printer_control.backends.main import Backend
from brother_label_printer_control.constants import Media
from brother_label_printer_control.printers.main import Printer
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from .interfacing.font import get_default_font
from .interfacing.motor_control import MotorPowerButtonControl


class Settings(BaseSettings):
    """Get the Settings from the Environment"""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    backend: Backend
    printer: Printer
    media: Media
    font: str = Field(default_factory=lambda: get_default_font())
    vendor_id: int | None = None
    product_id: int | None = None
    motor_initial: int | None = None
    motor_final: int | None = None

    @field_validator("vendor_id", "product_id", "motor_initial", "motor_final", mode="before")
    def parse_optional_int(cls, value: str | None) -> int | None:
        if value == "" or value is None:
            return None
        return int(value)

    @field_validator("backend", mode="before")
    def set_backend(cls, backend: str) -> Backend:
        return Backend.get(backend)

    @field_validator("printer", mode="before")
    def set_printer(cls, printer: str) -> Printer:
        return Printer.get(printer)

    @field_validator("media", mode="before")
    def set_media(cls, media: str) -> Media:
        return Media.get(media)

    @property
    def motor_control(self) -> MotorPowerButtonControl | None:
        return MotorPowerButtonControl.get(self.motor_initial, self.motor_final)


@lru_cache
def get_settings():
    return Settings()
