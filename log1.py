import logging
import json
from datetime import datetime

class LogIngestor:
    def __init__(self, api_name, log_file):
        self.api_name = api_name
        self.log_file = log_file
        self.logger = logging.getLogger(api_name)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log(self, level, log_string, metadata):
        log_data = {
            "level": level,
            "log_string": log_string,
            "timestamp": datetime.utcnow().isoformat(),
            "metadata": metadata
        }
        self.logger.info(json.dumps(log_data))

# Usage example
log_ingestor = LogIngestor("API_Name", "log1.log")
log_ingestor.log("info", "This is an informational message.", {"source": "example"})
