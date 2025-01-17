
import psutil
import time
import logging

# Configure logging for self-monitoring
logging.basicConfig(
    filename="self_monitoring.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def monitor_system():
    """
    Monitors system performance (CPU, memory, and disk usage) in real time.
    """
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        disk_usage = psutil.disk_usage("/")

        logging.info(f"CPU Usage: {cpu_usage}%")
        logging.info(f"Memory Usage: {memory_info.percent}%")
        logging.info(f"Disk Usage: {disk_usage.percent}%")

        time.sleep(5)  # Monitor every 5 seconds

if __name__ == "__main__":
    logging.info("Starting self-monitoring script...")
    monitor_system()
