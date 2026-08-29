from brother_label_printer_control.job import Job
from fastapi import APIRouter, Depends

from ..interfacing.printer_manager import PrinterManager
from ..requests.print_request import PrintRequest

router = APIRouter()


@router.get("/print")
@router.post("/print")
def print_label(
    request: PrintRequest,
    printer_manager: PrinterManager = Depends(PrinterManager.get),
):
    printer = printer_manager.printer

    label = request.generate_label(request.media)

    job = Job(request.media)
    job.add_page(label)

    printer.print(job)

    return {"status": "success", "message": "Label printed successfully"}
