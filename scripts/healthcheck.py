import requests
from loguru import logger
from dotenv import load_dotenv
import os
import time

load_dotenv()

API_BASE = os.getenv("API_BASE")


def safe_get(url, retries=3, timeout=5):
    """Make a safe HTTP GET request with retries and logs."""
    for attempt in range(1, retries + 1):
        try:
            logger.info(f"Attempt {attempt}: GET {url}")
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response.json()

        except Exception as e:
            logger.error(f"Failed attempt {attempt}: {e}")
            time.sleep(1.5)

    logger.critical(f"Request failed permanently after {retries} attempts.")
    return None


def fetch_countries():
    url = f"{API_BASE}/all"
    data = safe_get(url)

    if not data:
        logger.error("Could not fetch countries.")
        return

    logger.success(f"Fetched {len(data)} countries.")
    return data


if __name__ == "__main__":
    logger.info("Running healthcheck script...")
    countries = fetch_countries()