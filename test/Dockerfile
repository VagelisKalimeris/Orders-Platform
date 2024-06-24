# Choose base image
FROM python:3.11

# Create dir
WORKDIR /Test-Orders

# Install dependencies
COPY requirements.txt /Test-Orders/test/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /Test-Orders/test/requirements.txt

# Copy necessary files
COPY . /Test-Orders/test


# Run tests
#CMD ["/bin/bash","-c","pytest -vs"]

CMD ["/bin/bash","-c","tail -f /dev/null"]