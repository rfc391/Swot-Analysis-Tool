# SWOT Analysis Tool

## Overview

This project provides a SWOT analysis tool with AI-powered suggestions, collaborative features, and advanced analytics. It includes both desktop and web interfaces.

## Features

1. **AI-Assisted SWOT Generation**:
    - Generate Strengths, Weaknesses, Opportunities, and Threats using AI.
    - Use custom prompts for tailored suggestions.
    - Enable the AI to learn from user-provided data (future feature).

2. **User Experience Enhancements**:
    - Export SWOT data as JSON, Excel, or PDF.
    - Real-time collaboration for web-based SWOT analysis.

3. **Advanced Analytics**:
    - Visualize SWOT insights with charts and graphs.
    - Gain AI-driven insights from historical data.

4. **Scalable Design**:
    - Cloud-hosted MongoDB for data storage.
    - API authentication with JWT for security.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd SWOT_Project
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start MongoDB server and API:
   ```bash
   python api.py
   ```

## Usage

### Desktop Application
Launch the Tkinter-based GUI:
```bash
python desktop_gui.py
```

### Web Application
Run the web app locally:
```bash
python web_app.py
```

### REST API
Access AI-based SWOT suggestions:
```bash
curl -X POST http://localhost:5000/api/swot/suggest -H "Content-Type: application/json" -d '{"category": "opportunity", "description": "expanding into new markets"}'
```

## Contributing

Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.

## License

Licensed under the MIT License.