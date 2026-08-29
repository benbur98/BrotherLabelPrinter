from brother_label_printer_control.utils.font import get_fonts


def get_default_font() -> str | None:
    """Get the First Available TrueType Font in Linux as Default"""
    try:
        return list(get_fonts().values())[0][0].as_posix()
    except IndexError:
        return None
