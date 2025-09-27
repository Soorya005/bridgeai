# Use Ubuntu base image
FROM ubuntu:22.04

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    cmake \
    python3 \
    python3-pip \
    libcurl4-openssl-dev

# Set working directory
WORKDIR /app

# Install Python dependencies
RUN pip install flask   # <-- Add it here

# Clone and build llama.cpp (if needed)
RUN git clone https://github.com/ggerganov/llama.cpp.git llama.cpp
WORKDIR /app/llama.cpp
RUN mkdir build && cd build && cmake .. && cmake --build .
WORKDIR /app

# Copy your Python server script
COPY run_model.py .

# Expose the port your Flask app will run on
EXPOSE 5000

# Run the server
CMD ["python3", "run_model.py"]
