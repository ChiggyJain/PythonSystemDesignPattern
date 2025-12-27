
from fastapi import FastAPI
from app.api.v1.users import router as user_router

# app object
app = FastAPI(title="Layered Architecture Demo")


# FastAPI builds a routing table
# registered all apis
# Event loop (uvicorn) listens asynchronously
app.include_router(user_router, prefix="/api/v1")
