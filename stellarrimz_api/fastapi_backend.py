from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from anywhere (for testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000", "https://stellarrimz.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/data")
def get_data():
    return {
        "message": "Hello from Stell-E!",
        "image_url": "D:\Priyanka\My_GitHub\StellarRimz\my-test-app\Stell-E.png"
    }
