import asyncio
from gamecreator import NormalGameCreator


async def main():
    game = NormalGameCreator.setup()
    await game.start_game()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    