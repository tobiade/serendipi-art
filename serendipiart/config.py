import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # General Config
    SECRET_KEY = os.getenv("SECRET_KEY")
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_ENV = os.getenv("FLASK_ENV")

    # openai
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
