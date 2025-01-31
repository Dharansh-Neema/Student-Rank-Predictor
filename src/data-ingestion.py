import pandas as pd
from .logger import setup_logger

logger = setup_logger(
    log_file="logs/data-ingestion.log",
    console_level="DEBUG",
    file_level="DEBUG"
)