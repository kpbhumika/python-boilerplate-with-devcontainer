FROM python:3.12-slim-bookworm

COPY . /app



# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
build-essential \
&& rm -rf /var/lib/apt/lists/*


WORKDIR /app
# Install dependencies
RUN pip3 install -r requirements.txt
