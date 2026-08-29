FROM ghcr.io/astral-sh/uv:debian

RUN uv venv
RUN apt update && apt install -y usbutils curl fontconfig unzip

# Install JetBrains Mono Font
RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/JetBrains/JetBrainsMono/master/install_manual.sh)"

# Copy Code to Container
COPY ./web /app

# Build and Install ServoMotorControl
COPY ./motor /motor
WORKDIR /motor
RUN uv pip install .
WORKDIR /

WORKDIR /app
ENV PYTHONPATH="/app"

RUN uv sync

CMD ["print_server", "run", "main.py", "--port", "80"]
