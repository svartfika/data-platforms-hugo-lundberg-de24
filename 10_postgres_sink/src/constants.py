import os
from typing import Final

import dotenv

dotenv.load_dotenv()

KAFKA_HOST: Final[str] = str(os.getenv("KAFKA_HOST", "localhost"))
KAFKA_PORT: Final[int] = int(os.getenv("KAFKA_PORT", 9092))

COINMARKETCAP_API_KEY: Final[str] = os.getenv("COINMARKETCAP_API_KEY", "")
