FROM python:3.11-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    libportaudio2 \    
    # libsm6 libxext6 libxrender-dev \
    python3-opencv \
    && apt-get clean

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY . .
WORKDIR /app

# Set the display environment variable
ENV DISPLAY=:0

# Command to run your Python script
CMD ["python", "server.py"]
