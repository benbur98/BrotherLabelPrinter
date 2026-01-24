FROM python:3.13-slim

RUN apt update && apt install -y usbutils curl fontconfig unzip

RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/JetBrains/JetBrainsMono/master/install_manual.sh)"

# Copy Code to Container
COPY ./web /app

# Build and Install ServoMotorControl
COPY ./motor /motor
WORKDIR /motor
RUN pip install .
WORKDIR /

# Build and Install BrotherLabelPrinterControl Submodule
#RUN pip install https://github.com/ben-burwood/BrotherLabelPrinterControl/releases/download/0.8.0/brotherlabelprintercontrol-0.8.0-py3-none-any.whl
COPY ./BrotherLabelPrinterControl /BrotherLabelPrinterControl
WORKDIR /BrotherLabelPrinterControl
RUN pip install -r requirements.txt
RUN pip install .
WORKDIR /

RUN pip install --upgrade -r /app/requirements.txt

WORKDIR /app
ENV PYTHONPATH="/app"

CMD ["print_server", "run", "main.py", "--port", "80"]
