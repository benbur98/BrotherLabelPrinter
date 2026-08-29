import time
from typing import Annotated

from brother_label_printer_control.backends.main import Backend
from brother_label_printer_control.backends.usb import PyUSBBackend
from brother_label_printer_control.printers import GenericPrinter
from brother_label_printer_control.printers.main import Printer
from fastapi import Depends

from ..settings import Settings, get_settings
from .motor_control import MotorPowerButtonControl, toggle_power_button


class PrinterManager:
    _instance = None

    def __init__(
        self,
        backend_type: Backend,
        printer_type: Printer,
        motor_control: MotorPowerButtonControl | None = None,
        vendor_id: int | None = None,
        product_id: int | None = None,
    ) -> None:
        self._backend_type = backend_type
        self._printer_type = printer_type

        self._motor_control = motor_control

        self._vendor_id = vendor_id
        self._product_id = product_id

    def __new__(
        cls,
        backend_type: Backend,
        printer_type: Printer,
        motor_control: MotorPowerButtonControl | None = None,
        vendor_id: int | None = None,
        product_id: int | None = None,
    ) -> "PrinterManager":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__init__(backend_type, printer_type, motor_control, vendor_id, product_id)
            cls._instance._initialize_printer()
        return cls._instance

    def _initialize_printer(self) -> None:
        if self._motor_control is not None:
            toggle_power_button(self._motor_control)
            time.sleep(5)

        backend = self._backend_type.backend(self._vendor_id, self._product_id)
        if isinstance(backend, PyUSBBackend):
            backend.detach_from_kernel()

        self._printer = self._printer_type.printer(backend)

    @property
    def printer(self) -> GenericPrinter:
        return self._printer

    @classmethod
    def get(cls, settings: Annotated[Settings, Depends(get_settings)]) -> "PrinterManager":
        return cls(settings.backend, settings.printer, settings.motor_control)
