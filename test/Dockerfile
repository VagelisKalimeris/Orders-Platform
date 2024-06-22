# Choose base image
FROM python:3.11

# Create dir
WORKDIR /test-orders

# Install dependencies
COPY requirements.txt /test-orders/test/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /test-orders/test/requirements.txt

# Copy necessary files
COPY . /test-orders/test


# Run tests
CMD ["/bin/bash","-c","pytest -v"]