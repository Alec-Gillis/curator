from fastapi import APIRouter, Depends, HTTPException
from starlette.requests import Request
from starlette.responses import RedirectResponse
import requests
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI

# Create an API router for authentication-related endpoints
router = APIRouter()

# Endpoint to initiate Spotify login
@router.get("/login")
def login():
    # Define the required scope for the Spotify API
    scope = "user-read-private"
    redirect_uri = SPOTIFY_REDIRECT_URI
    # Construct the Spotify authorization URL
    auth_url = (
        "https://accounts.spotify.com/authorize"
        f"?response_type=code&client_id={SPOTIFY_CLIENT_ID}"
        f"&scope={scope}&redirect_uri={redirect_uri}"
    )
    # Redirect the user to the Spotify login page
    return RedirectResponse(auth_url)

# Endpoint to handle the callback from Spotify after login
@router.get("/callback")
def callback(request: Request):
    # Get the authorization code from the query parameters
    code = request.query_params.get("code")
    if not code:
        raise HTTPException(status_code=400, detail="Authorization code not found")
    
    # Request to exchange the authorization code for an access token
    token_url = "https://accounts.spotify.com/api/token"
    token_data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": SPOTIFY_REDIRECT_URI,
        "client_id": SPOTIFY_CLIENT_ID,
        "client_secret": SPOTIFY_CLIENT_SECRET,
    }
    token_response = requests.post(token_url, data=token_data)
    token_json = token_response.json()
    
    # Extract the access token from the response
    access_token = token_json.get("access_token")
    if not access_token:
        raise HTTPException(status_code=400, detail="Access token not found")
    
    # Use the access token to get the user's profile information from Spotify
    user_url = "https://api.spotify.com/v1/me"
    headers = {"Authorization": f"Bearer {access_token}"}
    user_response = requests.get(user_url, headers=headers)
    user_json = user_response.json()
    
    # Return the user's profile information as JSON
    return user_json  # or RedirectResponse to the frontend with a token
