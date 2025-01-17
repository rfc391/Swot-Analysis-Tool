
import unittest
from core import FileHandler
import os

class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_file.txt"
        self.copy_path = "copy_test_file.txt"
        self.move_path = "moved_test_file.txt"
        with open(self.test_file, "w") as f:
            f.write("Test content")

    def tearDown(self):
        for file in [self.test_file, self.copy_path, self.move_path]:
            if os.path.exists(file):
                os.remove(file)

    def test_copy_file(self):
        result = FileHandler.copy_file(self.test_file, self.copy_path)
        self.assertTrue(os.path.exists(self.copy_path))
        self.assertIn("copied", result)

    def test_move_file(self):
        result = FileHandler.move_file(self.test_file, self.move_path)
        self.assertTrue(os.path.exists(self.move_path))
        self.assertIn("moved", result)

    def test_delete_file(self):
        result = FileHandler.delete_file(self.test_file)
        self.assertFalse(os.path.exists(self.test_file))
        self.assertIn("deleted", result)

if __name__ == "__main__":
    unittest.main()

import pytest
from core import (
    send_kafka_message, send_rabbitmq_message, cache_data, get_cached_data,
    write_influx_data, execute_postgres_query, write_immutable_data, get_immutable_data,
    add_to_ipfs, get_from_ipfs
)

def test_kafka_integration():
    try:
        send_kafka_message('test-topic', 'Test Message')
    except Exception as e:
        pytest.fail(f"Kafka integration failed: {e}")

def test_rabbitmq_integration():
    try:
        send_rabbitmq_message('test-queue', 'Test Message')
    except Exception as e:
        pytest.fail(f"RabbitMQ integration failed: {e}")

def test_redis_integration():
    cache_data('test_key', 'test_value')
    assert get_cached_data('test_key').decode() == 'test_value'

def test_influxdb_integration():
    try:
        write_influx_data([{"measurement": "test", "fields": {"value": 1.0}}])
    except Exception as e:
        pytest.fail(f"InfluxDB integration failed: {e}")

def test_postgres_integration():
    try:
        execute_postgres_query("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, data TEXT);")
        execute_postgres_query("INSERT INTO test_table (data) VALUES (%s)", ('Test Data',))
    except Exception as e:
        pytest.fail(f"PostgreSQL integration failed: {e}")

def test_immudb_integration():
    write_immutable_data('test_key', 'test_value')
    assert get_immutable_data('test_key').value.decode() == 'test_value'

def test_ipfs_integration(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("This is a test.")
    file_hash = add_to_ipfs(str(test_file))
    content = get_from_ipfs(file_hash).decode()
    assert content == "This is a test."
