################################################################################
#         For API trial and documentation visit http://localhost/docs          #
################################################################################

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from order.routers import order_router


def customize_openapi_schema():
    """
    Updates OpenAPI documentation details for SWAGGER UI.
    """
    openapi_schema = get_openapi(
        title='Forex Trading Platform API',
        version='1.0.0',
        description='A RESTful API to simulate a Forex trading platform with WebSocket support for real-time order '
                    'updates.',
        servers=[
            {
                'url': 'http://0.0.0.0:80'
            }
        ],
        routes=app.routes
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


# Start API
app = FastAPI()

# Enable routes
app.include_router(order_router.router)


# Customize SWAGGER
app.openapi = customize_openapi_schema