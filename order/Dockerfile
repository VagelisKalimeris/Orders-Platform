# Choose base image
FROM python:3.11

# Create dir
WORKDIR /Orders-Api

# Install dependencies
COPY requirements.txt /Orders-Api/order/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /Orders-Api/order/requirements.txt

# Copy necessary files
COPY . /Orders-Api/order


# Start server
CMD ["/bin/bash", "-c", "uvicorn order.main:app --reload --host 0.0.0.0 --port 80"]