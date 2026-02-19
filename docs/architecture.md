# System Architecture

## Architecture Type
Layered Architecture

## Components

### Frontend
- HTML templates rendered using Flask
- Provides dashboard, add item form, and restock recommendations

### Backend
- Flask application handles routes and business logic
- Connects frontend with database and intelligent agent

### Intelligent Agent
- Rule-based agent
- Compares stock quantity with minimum threshold
- Suggests restocking quantity when required

### Database
- SQLite database
- Stores inventory details persistently

## Data Flow
User → Web Interface → Flask Backend → Intelligent Agent → Database → Response to User
