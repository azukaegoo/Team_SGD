# Use pinned and minimal Alpine base image as requested
FROM python:3.10.13-alpine3.19

# Set working directory inside the container
WORKDIR /app

# Install necessary build dependencies (using no-cache to remove bloat)
RUN apk add --no-cache gcc musl-dev linux-headers

# Copy pinned requirements first to optimize build time
COPY requirements.txt .

# Install dependencies without caching to minimize final image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run the application
CMD ["python", "run.py"]