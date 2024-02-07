import asyncio

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
        host="0.0.0.0",
        port=8000,
        log_level="info",
    )
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
