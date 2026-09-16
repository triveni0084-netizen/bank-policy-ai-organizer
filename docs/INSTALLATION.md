# Installation Guide

## Prerequisites

- Docker & Docker Compose
- Python 3.9+ (for local development)
- Node.js 16+ (for frontend development)
- PostgreSQL 13+ (for local database)
- MongoDB 5.0+ (for local database)

## Quick Start with Docker

### 1. Clone Repository
```bash
git clone https://github.com/triveni0084-netizen/bank-policy-ai-organizer.git
cd bank-policy-ai-organizer
```

### 2. Setup Environment
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

### 3. Start Services
```bash
docker-compose up -d
```

### 4. Access Application
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Swagger UI: http://localhost:8000/redoc

## Local Development Setup

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
alembic upgrade head

# Start server
uvicorn main:app --reload
```

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

## Database Setup

### PostgreSQL
```bash
creatdb bank_policy_db
psql bank_policy_db < database/schema.sql
```

### MongoDB
```bash
mongod --dbpath ./data/db
```

## Configuration

Edit `.env` file with your settings:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/bank_policy_db
MONGODB_URL=mongodb://localhost:27017

# AI/ML
OPENAI_API_KEY=your-key-here

# Security
SECRET_KEY=your-secret-key
```

## Troubleshooting

### Port Already in Use
```bash
# Change ports in docker-compose.yml or kill existing process
lsof -i :3000  # Check port 3000
kill -9 <PID>
```

### Database Connection Issues
```bash
# Test connection
psql -U user -d bank_policy_db -h localhost
```

### Docker Issues
```bash
# Clean up
docker-compose down -v
docker-compose up -d --build
```