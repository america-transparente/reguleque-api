import uvicorn
import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from fastapi import FastAPI

from reguleque_api.config import get_config
from reguleque_api.db import db
from reguleque_api.internal import admin
from reguleque_api.routers import entries


# from .routers import entries

app = FastAPI()

# Add logging with Sentry
sentry_sdk.init(
    dsn="https://473b4f1f09ce4dbc8a317a26684f5a83@o584603.ingest.sentry.io/5737292",
)
app.add_middleware(SentryAsgiMiddleware)

# Load the admin route
app.include_router(admin.router)

# Load the main routes por entries
app.include_router(entries.router)


@app.on_event("startup")
async def startup():
    config = get_config()
    await db.connect_to_database(path=config.db_path)


@app.on_event("shutdown")
async def shutdown():
    await db.close_database_connection()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
