#!/usr/bin/env python3
"""
Bank Policy AI Organizer - Main Application Entry Point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
import logging
from contextlib import asynccontextmanager

from config import settings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Lifespan context manager for startup/shutdown events
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting Bank Policy AI Organizer...")
    logger.info(f"Environment: {settings.FASTAPI_ENV}")
    logger.info(f"Debug Mode: {settings.DEBUG}")
    yield
    # Shutdown
    logger.info("Shutting down Bank Policy AI Organizer...")

# Initialize FastAPI application
app = FastAPI(
    title="Bank Policy AI Organizer",
    description="Enterprise-Grade AI-Powered Bank Policy Management System",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Add middleware
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Bank Policy AI Organizer",
        "version": "2.0.0"
    }

# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Bank Policy AI Organizer",
        "version": "2.0.0",
        "docs": "/docs",
        "api_base": "/api"
    }

# API v1 endpoints (to be imported from routes)
# TODO: Import and include routers
# from app.api.routes import auth, policies, compliance, analytics, ai
# app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
# app.include_router(policies.router, prefix="/api/v1/policies", tags=["Policies"])
# app.include_router(compliance.router, prefix="/api/v1/compliance", tags=["Compliance"])
# app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["Analytics"])
# app.include_router(ai.router, prefix="/api/v1/ai", tags=["AI Services"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )