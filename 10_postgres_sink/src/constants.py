import os
from typing import Final

import dotenv

dotenv.load_dotenv()

KAFKA_HOST: Final[str] = str(os.getenv("KAFKA_HOST", "localhost"))
KAFKA_PORT: Final[int] = int(os.getenv("KAFKA_PORT", 9092))

POSTGRES_HOST: Final[str] = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT: Final[int] = int(os.getenv("POSTGRES_PORT", 5432))
POSTGRES_USER: Final[str] = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD: Final[str] = os.getenv("POSTGRES_PASSWORD", "")
POSTGRES_DB: Final[str] = os.getenv("POSTGRES_DB", "")

COINMARKETCAP_API_KEY: Final[str] = os.getenv("COINMARKETCAP_API_KEY", "")