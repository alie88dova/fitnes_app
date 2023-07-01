from fastapi import FastAPI

from starlette.staticfiles import StaticFiles
from auth.router import router as auth_router
from main_app.router import router as main_app_router
from operations.router import router as operations_router
from tasks.router import router as test_task_router
from aiohttp import web
from aiohttp_asgi import ASGIResource
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

app = FastAPI(
    title="Fitnes Today ",
)
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth_router)
app.include_router(main_app_router)
app.include_router(operations_router)
app.include_router(test_task_router)


@app.on_event("startup")
async def startup():
    print("start startup")
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


aiohttp_app = web.Application()

# Create ASGIResource which handle
# Все request с "/" будут использовать fastapi
asgi_resource = ASGIResource(app, root_path="/")
# Register resource
aiohttp_app.router.register_resource(asgi_resource)

# Mount startup and shutdown events from aiohttp to ASGI app
asgi_resource.lifespan_mount(aiohttp_app)

# Start the application
web.run_app(aiohttp_app)