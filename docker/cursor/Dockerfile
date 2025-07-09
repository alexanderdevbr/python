FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    libx11-6 \
    libxrender1 \
    libxtst6 \
    libxi6 \
    python3-tk python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pyautogui

COPY script.py /app/script.py
WORKDIR /app

CMD ["python", "script.py"]
