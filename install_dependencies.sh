
#!/bin/bash

echo "Installing dependencies..."

# Install core Python packages
pip install -r requirements.txt

# Install missing dependencies individually as needed
pip install redis
pip install kafka-python
pip install pika
pip install influxdb
pip install psycopg2
pip install immudb
pip install transformers
pip install bson

echo "All dependencies installed successfully."
