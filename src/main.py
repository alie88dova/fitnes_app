from fastapi import FastAPI

from starlette.staticfiles import StaticFiles
from auth.router import router as auth_router
from main_app.router import router as main_app_router
from operations.router import router as operations_router
from aiohttp import web
from aiohttp_asgi import ASGIResource



app = FastAPI(
    title="Fitnes Today ",
)
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth_router)
app.include_router(main_app_router)
app.include_router(operations_router)

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