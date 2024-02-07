import asyncio
from settings import app_settings
import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="Book Storing API",
    description="A simple API that stores books",
    version="0.1",
)


async def main():
    """Run the server"""
    config = uvicorn.Config(
        app,
        host=app_settings.host,
        port=app_settings.port,
        log_level=app_settings.log_level,
    )
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
