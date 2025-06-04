# Weather Analysis

Weather data analysis for Krakow (and Lviv) using Python.

## Description

This project loads weather data from CSV, cleans it, and generates plots for yearly average temperature and monthly temperature distribution. All results are saved in the `plots/` folder.

## Installation

1. Create virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate virtual environment on Linux/macOS:
   ```bash
   source venv/bin/activate
   ```
   Activate virtual environment on Windows:
   ```bash
   venv\Scripts\activate.bat
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python src/main.py
```

## Structure

- `src/` — main code (loading, processing, visualization)
- `data/krakow_weather.csv` — input data
- `plots/` — visualization results

## Dependencies

All dependencies are listed in `requirements.txt`.

## Code formatting

Format code with [Black](https://black.readthedocs.io/en/stable/) and [isort](https://pycqa.github.io/isort/):

```bash
black src/
isort src/
```
