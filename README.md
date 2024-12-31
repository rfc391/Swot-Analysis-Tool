
# SWOT Analysis Tool

An AI-powered SWOT (Strengths, Weaknesses, Opportunities, and Threats) analysis tool built on Replit, designed to streamline strategic planning for businesses and individuals.

## Features

- AI-powered SWOT suggestions
- Multi-device support with responsive web interface
- RESTful API for programmatic access
- MongoDB integration for data persistence
- Real-time collaborative analysis

## Quick Start

1. Fork this Repl to your account
2. Click the Run button
3. Access the web interface through the provided URL

## Setup

The project automatically installs dependencies on first run. Required packages are listed in `requirements.txt`.

Make sure MongoDB is running:
```bash
mongod &
```

## Usage

### Web Interface
Access the web application through your Replit URL to:
- Create new SWOT analyses
- View existing analyses
- Get AI-powered suggestions
- Collaborate with team members

### API Endpoints

```bash
# Create a new SWOT analysis
POST /api/swot

# Get AI suggestions
POST /api/swot/suggest
{
    "category": "opportunity",
    "description": "expanding into new markets"
}

# Get all SWOT entries
GET /api/swot
```

### AI Integration

```python
from swot_ai_helper import SWOTAIHelper

ai_helper = SWOTAIHelper()
suggestions = ai_helper.suggest_swot("opportunity", "market expansion")
```

## Contributing

1. Fork this Repl
2. Make your changes
3. Test thoroughly
4. Create a pull request

## License

MIT License - See LICENSE file for details
