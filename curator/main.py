from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware

from curator.api.auth import router as auth_router

# Create FastAPI app
app = FastAPI()

origins = [
    "localhost",
    "localhost:8000",
]

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the static files directory to serve the frontend files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include the authentication router
app.include_router(auth_router, prefix="/api/auth")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Define a test endpoint for fetching user data (mock endpoint)
@app.get("/api/user")
def read_user():
    # Mock endpoint for testing, replace with actual user data retrieval
    return {"username": "test_user"}
