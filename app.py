import asyncio
from service import service

async def main():
    stats = await service().get_stats_async("yarosfarian")

    print(stats.inputs.all.overall.matches)

if __name__ == "__main__":
    asyncio.run(main())