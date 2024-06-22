# Choose base image
FROM python:3.11

# Create dir
WORKDIR /Orders-Api

# Install dependencies
COPY requirements.txt /Orders-Api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /Orders-Api/requirements.txt

# Copy necessary files
COPY . /Orders-Api/


# Start server
CMD ["/bin/bash", "-c", "uvicorn main:app --reload --host 0.0.0.0 --port 80"]