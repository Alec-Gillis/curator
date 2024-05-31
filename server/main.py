from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from auth import router as auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="../client/public"), name="static")

app.include_router(auth_router, prefix="/auth")

@app.get("/api/user")
def read_user():
    # Mock endpoint for testing, replace with actual user data retrieval
    return {"username": "test_user"}
