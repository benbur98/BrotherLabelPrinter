FROM ghcr.io/astral-sh/uv:debian-slim

RUN apt update && apt install -y --no-install-recommends \
    ca-certificates git usbutils curl fontconfig unzip \
  && rm -rf /var/lib/apt/lists/*

# Install JetBrains Mono Font
RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/JetBrains/JetBrainsMono/master/install_manual.sh)"
ENV FONT=/root/.local/share/fonts/fonts/ttf/JetBrainsMono-Regular.ttf

COPY . /app
WORKDIR /app

RUN uv sync --frozen

WORKDIR /app/web

HEALTHCHECK --interval=60s --timeout=5s --start-period=10s --retries=2 \
  CMD curl -f http://localhost:80/health || exit 1

CMD ["uv", "run", "fastapi", "run", "main.py", "--port", "80"]
