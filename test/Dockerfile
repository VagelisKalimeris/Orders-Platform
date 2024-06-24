# Choose base image
FROM python:3.11

# Create dir
WORKDIR /Test-Orders

# Install dependencies
COPY requirements.txt /Test-Orders/test/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /Test-Orders/test/requirements.txt

# Copy necessary files
COPY . /Test-Orders/test


# Run tests and stay alive for debugging or reruns
CMD ["/bin/bash","-c","sleep 3; pytest -vs --html=/test/test_reports/report.htm; tail -f /dev/null"]
