# Setup Instructions for Flet Python App

## Overview
This is a Python application built with Flet UI framework. Flet allows you to build beautiful, multi-platform applications with a simple Python API.

## Prerequisites
- Python 3.8 or higher
- Anaconda or pip package manager
- Git (for cloning the repository)

## Installation Steps

### Option 1: Using Anaconda (Recommended)

#### 1. Create Virtual Environment
```bash
conda create -n flet-app python=3.11
conda activate flet-app
```

#### 2. Clone Repository
```bash
git clone https://github.com/rehabselise/flet-python-app.git
cd flet-python-app
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Configure Environment
```bash
cp .env.example .env
# Edit .env file with your configuration
```

#### 5. Run Application
```bash
python main.py
```

### Option 2: Using pip directly

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
python main.py
```

## Project Structure
```
flet-python-app/
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── .env.example            # Environment configuration template
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
└── SETUP_INSTRUCTIONS.md   # This file
```

## Development

### Running the App
```bash
python main.py
```

### Debugging
To enable debug mode, edit `.env`:
```
APP_DEBUG=True
```

### Adding Dependencies
When adding new packages:
```bash
pip install package-name
pip freeze > requirements.txt
```

## Troubleshooting

### Issue: Module not found
**Solution:** Ensure virtual environment is activated and dependencies are installed:
```bash
conda activate flet-app
pip install -r requirements.txt
```

### Issue: Flet not installing
**Solution:** Try installing from source:
```bash
pip install flet --upgrade
```

### Issue: Port already in use
**Solution:** Flet uses port 8550 by default. Check for existing processes or specify a different port.

## Resources
- [Flet Documentation](https://flet.dev)
- [Flet Examples](https://github.com/flet-dev/examples)
- [Python Documentation](https://docs.python.org/3/)

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License
MIT License
