import logging

# Configure logging format and level
logging.basicConfig(
    level=logging.INFO,  # Change to DEBUG for more details
    format="%(asctime)s - %(levelname)s - %(module)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Get a logger instance
logger = logging.getLogger("shopify_scraper")
