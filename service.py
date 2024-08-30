import os
from dotenv import load_dotenv
import fortnite_api


class service:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("API_KEY")


    async def get_stats_async(self, user_name, plataform="epic"):
        async with fortnite_api.Client(api_key=self.api_key) as client:
            stats = await client.fetch_br_stats(name=user_name)

            return stats