from dataclasses import dataclass, field
from dotenv import load_dotenv
import os

load_dotenv()


@dataclass
class Config:

    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    BOT_NAME: str = os.getenv("BOT_NAME", "VTH Ads Bot")
    BOT_USERNAME: str = os.getenv("BOT_USERNAME", "vthadsbot")

    DATABASE_URL: str = os.getenv("DATABASE_URL", "")

    API_ID: int = int(os.getenv("API_ID", "0"))
    API_HASH: str = os.getenv("API_HASH", "")

    ADMINS: list[int] = field(
        default_factory=lambda: [
            int(x)
            for x in os.getenv("ADMINS", "").split(",")
            if x.strip()
        ]
    )

    LOG_CHANNEL: int = int(os.getenv("LOG_CHANNEL", "0"))

    FORCE_JOIN_1: str = os.getenv("FORCE_JOIN_1", "")
    FORCE_JOIN_2: str = os.getenv("FORCE_JOIN_2", "")

    UPI_ID: str = os.getenv("UPI_ID", "")
    UPI_NAME: str = os.getenv("UPI_NAME", "VTH NETWORK")

    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"


config = Config()