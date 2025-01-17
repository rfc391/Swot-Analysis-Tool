
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("application.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def log_example():
    """
    Example function to demonstrate logging.
    """
    logger.info("Application started successfully.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")

if __name__ == "__main__":
    log_example()
