FROM python:3.10-slim
WORKDIR /workspace

# Install system dependencies (git and graphviz)
RUN apt-get update && apt-get install -y git graphviz && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["sleep", "infinity"]