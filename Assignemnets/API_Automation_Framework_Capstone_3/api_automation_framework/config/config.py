import os

BASE_URL = os.getenv("BASE_URL", "https://restful-booker.herokuapp.com")
USERNAME = os.getenv("BOOKER_USERNAME", "admin")
PASSWORD = os.getenv("BOOKER_PASSWORD", "password123")

TIMEOUT = int(os.getenv("API_TIMEOUT", "15"))

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}
