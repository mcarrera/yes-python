# Yes-Python API (Educational Experiment)

This project serves as an educational experiment, a Python port of an existing .NET API called "yes-order." Originally developed as an exercise a few months ago, I've recreated it in Python using FastAPI.

## Purpose
The primary purpose of this project is for me to become familiar with Python. Through this experiment, I aim to compare the same functionality implemented in both .NET and Python.

## Features
- [x] API endpoints similar to the original .NET API
- [x] Data processing and business logic in Python
- [x] Integration with FastAPI for web routing

## Project Structure
YES-PYTHON
├── main.py            # FastAPI app setup
├── app/               # Main application directory
│   ├── api/           # API routes (controllers)
│   ├── models/        # Pydantic models (data validation)
│   ├── services/      # Business logic
│   └── database.py    # Database setup
├── tests/             # Unit tests
└── .gitignore         # Git ignore rules

