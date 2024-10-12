# import libraries
# import asyncio
import logging
import os

# import from libraries
from dotenv import load_dotenv



async def get_tokens(name_of_token: str) -> str:
    """
    function accept name as str
    load .env file
    find token {name}

    :param name_of_token:
    :return: token as str
    """
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
        return os.getenv(name_of_token)
    else:
        print("No .env file found")
