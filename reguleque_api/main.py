import uvicorn
import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from fastapi import FastAPI

from reguleque_api.config import get_config
from reguleque_api.internal import admin
from reguleque_api.routers import entries

config = get_config()

app = FastAPI(title=config.app_name)

# Add logging with Sentry
if config.sentry_dsn:
    sentry_sdk.init(
        dsn=config.sentry_dsn,
    )
    app.add_middleware(SentryAsgiMiddleware)

# Load the admin route
app.include_router(admin.router)

# Load the main routes por entries
app.include_router(entries.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
