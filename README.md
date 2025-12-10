# Used Car Advertisement Dashboard  
**TripleTen Sprint 4 Project – Software Development Tools**

## Project Description  
This web dashboard explores a dataset of used car advertisements (`vehicles_us.csv`) scraped from online listings. It allows users to interactively analyze car prices, mileage trends, and condition relationships through visualizations built with **Plotly Express** and served via **Streamlit**.

The goal of the project is to practice:
- Jupyter Notebook EDA  
- Data cleaning and outlier handling  
- Building an interactive web dashboard with Streamlit  
- Version control with Git & GitHub  
- Deploying a Python web app (Render.com)

## Features  
- Interactive **price distribution histogram**  
- **Price vs Mileage** scatter plot colored by car condition  
- Checkbox to show/hide high-price & high-mileage outliers  
- Cleaned dataset:  
  - Model years: 2000–2025  
  - Price range: $100 – $100,000  
  - Mileage: 0 – 500,000 miles  
  - Missing values intelligently filled

## Project Structure  
.
├── vehicles_us.csv          # Dataset (must be in root)
├── app.py                   # Streamlit dashboard (main app)
├── notebooks/               # (optional) EDA.ipynb with exploratory analysis
├── README.md                # This file
├── .gitignore               # Ignores .venv/, pycache, etc.
└── requirements.txt         # (recommended – see below)

## How to Run Locally  
**Prerequisites:** Python 3.8+ installed.

1. Clone the repository  
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
2. Create and activate a virtual environment
   python -m venv .venv
   source .venv/bin/activate    # Mac/Linux
   .venv\Scripts\activate       # Windows
3. Install dependencies
   pip install streamlit pandas plotly
   pip install -r requirements.txt

4. Launch the dashboard
   streamlit run app.py
   

## Live URL
Live link: [https://sdt4-1.onrender.com](https://sdt4-1.onrender.com)

##Tech Stack

Python
Streamlit (for the web app)
Pandas (data manipulation)
Plotly (interactive visualizations)