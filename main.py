import fastapi
from fastapi import responses
import uvicorn
from starlette.staticfiles import StaticFiles
from api import proposal_api
from views import home

api = fastapi.FastAPI()


def configure():
    configure_routing()
    # TBD configure other stuff here


def configure_routing():
    api.mount("/static", StaticFiles(directory="static"), name="static")
    api.include_router(home.router)
    api.include_router(proposal_api.router)


# sourcery skip: hoist-statement-from-if
if __name__ == "__main__":
    configure()
    uvicorn.run(api, port=8000, host="127.0.0.1")
else:
    configure()
