from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from .auth import router as auth_router

# Create FastAPI app
app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust according to your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the static files directory to serve the frontend files
app.mount("/static", StaticFiles(directory="../client/public"), name="static")

# Include the authentication router
app.include_router(auth_router, prefix="/auth")

# Define a test endpoint for fetching user data (mock endpoint)
@app.get("/api/user")
def read_user():
    # Mock endpoint for testing, replace with actual user data retrieval
    return {"username": "test_user"}
