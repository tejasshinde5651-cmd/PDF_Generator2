# Main application entry point
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.pdf_routes import router


app = FastAPI(
    title="PDF Generator API",
    description="API to generate PDF from health camp form data",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api", tags=["PDF Generation"])