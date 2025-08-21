from fastapi import FastAPI
import logging
from app.manager import Manager


app = FastAPI()
manager = Manager()
logger = logging.getLogger(__name__)


@app.get("/process_data")
def process_data():
    """
    Endpoint to process data from the database and return processed results.
    """
    logger.info("Received request to process data.")
    try:
        processed_data = manager.get_processed_data()
        logger.info("Send data Successfully.")
        return {"data": processed_data}
    except Exception as e:
        logger.error(f"Error sending data: {e}")
        return {"error": str(e)}