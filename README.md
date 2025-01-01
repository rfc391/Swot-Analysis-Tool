
# SWOT Analysis Tool

A comprehensive, AI-powered SWOT (Strengths, Weaknesses, Opportunities, and Threats) analysis platform designed for modern business strategy development and execution.

## Overview

This tool leverages artificial intelligence to provide data-driven insights for strategic planning, helping businesses and individuals make informed decisions through structured SWOT analysis.

## Key Features

- **AI-Powered Analysis**: Intelligent suggestions for each SWOT category.
- **Real-time Collaboration**: Simultaneous multi-user analysis capabilities.
- **RESTful API**: Programmatic access for system integration.
- **Data Persistence**: MongoDB-backed storage for reliable data management.
- **Responsive Design**: Seamless experience across all devices.

## Quick Start

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Start MongoDB:
    ```bash
    mongod &
    ```
3. Run the application:
    ```bash
    python main.py
    ```

## AI-Powered Suggestions

The enhanced AI module provides insightful suggestions:
```python
from swot_ai_helper import SWOTAIHelper

ai_helper = SWOTAIHelper()
suggestion = ai_helper.suggest_swot("opportunity", "expanding into global markets")
print(suggestion)
```

**Output:**
```
Opportunity insight: Based on expanding into global markets, consider focusing on potential.
```

## API Endpoints

### Create SWOT Analysis
- **POST /api/swot**
- **Body:**
  ```json
  {
    "strengths": "string",
    "weaknesses": "string",
    "opportunities": "string",
    "threats": "string"
  }
  ```

### Get Suggestions
- **POST /api/swot/suggest**
- **Body:**
  ```json
  {
    "category": "strength",
    "description": "string"
  }
  ```

## Testing

Run the test suite:
```bash
python -m unittest discover tests
```

## License

Released under the MIT License. See LICENSE file for details.
