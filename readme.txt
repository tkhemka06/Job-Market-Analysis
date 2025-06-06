# Job Market Analysis - Unemployment Busters

## Project Overview
This project is designed to scrape job postings from various sources, including Indeed, LinkedIn, ZipRecruiter, Glassdoor, Google and multiple such job portals available on the internet. The application provides a streamlined interface for retrieving job data based on user-defined criteria such as search terms, location, and time of posting as well as the user being able to quickly apply to the given job.

## Table of Contents
  - Note
  - Features
  - Setup Instructions
    - Spyder Code Setup
    - Google Colab Setup
  - Usage
  - Analysis & Visualization
  - Dependencies
  - Future Work
  - Contributing
  - Team Members
  - License

## Note
The project integrates Google Colab and Google Drive for easier collaboration and file management. Ensure the required directories exist before running the project.  
We have were having a few issues running the google colab code at the end moment because of a few crucial APIs not working (i.e. job scraping related). We are submitting a spyder code for the same that lacks in comparison to it.
Sorry for the inconvenience and thank you for the consideration.

## Features
  - Scrapes job postings from multiple platforms (Indeed, LinkedIn, ZipRecruiter, Glassdoor, Google)
  - Provides flexibility in search parameters (keywords, location, etc.)
  - Uses Flask to set up a web-based interface for users
  - Includes email notification support for sending results
  - Leverages Google Colab and Google Drive integration for storing and retrieving project files
  - Text Analysis: Natural language processing techniques to extract meaningful information from job descriptions
  - Skill Extraction: Identification of in-demand technical and soft skills
  - Market Segmentation: Categorization of job listings by industry, role type, and seniority level
  - Trend Visualization: Graphical representation of job market trends over time

## Setup Instructions for Spyder Code

1. Clone the code into your device

2. Install the given libraries using the conda prompt:
```bash
pip install PyQt5 PyQtWebEngine pandas requests numpy matplotlib
```

3. Ensure that the Project folder and given open_web_ninja.csv is in the same directory

4. Run the given main code

5. The WebScraping takes alot of time due to bot protection by the websites that we are scraping. So please be patient and wait for 1-2min

## Setup Instructions for Google Colab
1. Clone the given google colab repository.

2. Upload the given folder into your drive as Python_Proj which should contain template, static folders and open_web_ninja.csv file

3. Email configurations for sending job details via SMTP.

4. Run the main script in a Python environment. Use Google Colab for ease of Drive integration if desired.

5. Access the web interface or the script's console output to interact with the job scraper.
Use the public access key that would look like the following:
"https://6141-34-90-232-69.ngrok-free.app"

6. The WebScraping takes alot of time due to bot protection by the websites that we are scraping. So please be patient and wait for 1-2min

## Usage
  - Run the given colab notebook/ python file with the above mentioned instructions
  - In given web-app utilize the search bars of desired search terms and location parameters.
  - Run the script to fetch job details.
  - Results can be saved to files or emailed.

## Analysis & Visualization

The project includes several types of analyses:
  1. Demand Analysis: Identifying the most in-demand roles and skills
  2. Geographic Distribution: Mapping job opportunities by location
  3. Skill Correlation: Finding relationships between different skill requirements

Visualizations are generated using:
  - Matplotlib
  - Pandas
  - NumPy
  - Other integrated data visualization tools

## Dependencies
Primary dependencies include:
  - PyQt5
  - PyQtWebEngine
  - pandas
  - requests
  - numpy
  - matplotlib
  - Flask (for web interface)
  - SMTP libraries (for email functionality)

Refer to `requirements.txt` for all necessary Python packages.

## Future Work
  - Implement real-time data collection pipeline
  - Enhance web scraping capabilities to bypass bot protection more efficiently
  - Develop more advanced filtering and sorting options
  - Create more interactive dashboards for exploring the data
  - Expand analysis to include international job markets

## Contributing
Contributions to this project are welcome! Please follow these steps:
  1. Fork the repository
  2. Create a feature branch (`git checkout -b feature/your-feature`)
  3. Commit your changes (`git commit -m 'Add some feature'`)
  4. Push to the branch (`git push origin feature/your-feature`)
  5. Open a Pull Request

## Members of Unemployment Busters Team
- Jiya Aggarwal - jagarwal@andrew.cmu.edu
- Summer Lee - summerle@andrew.cmu.edu
- Tanisha Khemka - tkhemka@andrew.cmu.edu
- Aditya Sannabhadti - asannabh@andrew.cmu.edu

---

Created by [Unemployment Busters Team](https://github.com/tkhemka06/Job-Market-Analysis)
