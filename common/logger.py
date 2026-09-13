import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("api_test")
logger.setLevel(logging.INFO)

if not logger.handlers:
    fh = logging.FileHandler("logs/test.log", encoding="utf-8")
    ch = logging.StreamHandler()
    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    fh.setFormatter(fmt)
    ch.setFormatter(fmt)
    logger.addHandler(fh)
    logger.addHandler(ch)