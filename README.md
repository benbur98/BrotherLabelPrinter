# Brother Printer

API and GUI for Brother PTP-700 Label Printer

This Repo is a Wrapper for and uses my [Fork](https://github.com/ben-burwood/BrotherLabelPrinterControl) of [labelprinterkit](https://github.com/ogelpre/labelprinterkit) for Interfacing the Printer.

# Print Settings

Labels MUST use the full pixel/points PrintArea for the given Media.
e.g. the 12mm has 70 pixel/points so the content (Text) MUST fill the 70 pixel/points.

# Install

Clone the repository.
Configure the config.yaml in the backend Module.

## SystemD Service

Run `./setup.sh` to Configure the Python Environment and SystemD Service.

The Service will then run as Root and Restart Policy to auto-start on Boot.

## Docker

### USB Device

Check the Device Path for the USB BrotherLabelPrinter in the docker-compose.yaml File, to ensure this is passed through.

The device path is usually in the format /dev/bus/usb/00x/00y, where 00x is the bus number and 00y is the device number.

`Bus 004 Device 007: ID 0000:0000 Brother Industries, Ltd PT-P700 P-touch Label Printer`
    In the example, the device path would be /dev/bus/usb/004/007.
