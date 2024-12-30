"""
##### DESCRIPTION
#This project is designed to 
#scrape job postings from various sources, including Indeed, LinkedIn, ZipRecruiter, Glassdoor, Google 
#and multiple such job portals available on the internet. 
The application provides a streamlined interface for retrieving job data based on user-defined 
criteria such as search terms, location, and time of posting as well as the user being able 
to quickly apply to the given job. It can only  be used for country of USA for now. This code
is just a husk of its true server code which has also been uploaded for the project.

##### Team Members:
Jiya Aggarwal - jagarwal@andrew.cmu.edu
Summer Lee - summerle@andrew.cmu.edu
Tanisha Khemka - tkhemka@andrew.cmu.edu
Aditya Sannabhadti - asannabh@andrew.cmu.edu
"""


## Required Libraries
import sys
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QComboBox, QTableWidget, QTableWidgetItem,
    QWidget, QFormLayout, QHeaderView, QMessageBox
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
import requests
import webbrowser


# API Keys
GOOGLE_MAPS_API_KEY = "AIzaSyAkhVVl0ombrXrKoLIOQmhp3btAJ6alyF4"
RAPIDAPI_KEY = "cdad6700bdmsh5ac106aa01f9ea7p104d83jsn15813f7690aa"  # Replace with your own key


# Fetch Jobs from Open Web Ninja API
def fetch_jobs_from_api(search_term, location, country="US", num_pages=1):
    url = "https://jsearch.p.rapidapi.com/search"
    querystring = {
        "query": f"{search_term} jobs in {location}",
        "page": "1",
        "num_pages": num_pages,
        "country": country,
        "date_posted": "all"
    }
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "jsearch.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        data = response.json().get("data", [])
        return pd.DataFrame(data)
    else:
        QMessageBox.warning(None, "API Error", f"Failed to fetch jobs: {response.status_code}")
        return pd.DataFrame()

##Loading QSS Sylesheet used for PyQT
def load_stylesheet(app):
    """Load the QSS stylesheet."""
    try:
        with open("modern_style.qss", "r") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("Stylesheet file 'modern_style.qss' not found. Using default style.")


## Main Application
class JobTrackerApp(QMainWindow):
    def __init__(self):
        super(JobTrackerApp, self).__init__()
        self.setWindowTitle("Modern Job Tracker")
        self.setGeometry(100, 100, 1200, 800)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Header
        header = QLabel("Modern Job Tracker Dashboard")
        header.setFont(QFont("Arial", 20, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        # Filters
        filter_layout = QFormLayout()
        self.search_term_input = QLineEdit()
        self.search_term_input.setPlaceholderText("Enter job title...")
        self.location_input = QLineEdit()
        self.location_input.setPlaceholderText("Enter location...")
        self.employment_type_combo = QComboBox()
        self.employment_type_combo.addItems(["", "Full-time", "Part-time", "Contract"])
        self.num_pages_input = QLineEdit()
        self.num_pages_input.setPlaceholderText("Number of pages")

        filter_layout.addRow("Search Term:", self.search_term_input)
        filter_layout.addRow("Location:", self.location_input)
        filter_layout.addRow("Employment Type:", self.employment_type_combo)
        filter_layout.addRow("Number of Pages:", self.num_pages_input)
        layout.addLayout(filter_layout)

        # Buttons
        button_layout = QHBoxLayout()
        search_button = QPushButton("Search")
        search_button.setIcon(QIcon.fromTheme("search"))
        search_button.clicked.connect(self.search_jobs)

        map_button = QPushButton("Show/Hide Map")
        map_button.setIcon(QIcon.fromTheme("map"))
        map_button.clicked.connect(self.toggle_map)

        button_layout.addWidget(search_button)
        button_layout.addWidget(map_button)
        layout.addLayout(button_layout)

        # Google Map
        self.map_view = QWebEngineView()
        self.map_view.setHtml(self.generate_map_html())
        self.map_view.setVisible(False)
        layout.addWidget(self.map_view)

        # Job Table
        self.jobs_table = QTableWidget()
        self.jobs_table.setColumnCount(6)
        self.jobs_table.setHorizontalHeaderLabels(["Job Title", "Company", "Location", "Employment Type", "Posted Date", "Actions"])
        self.jobs_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.jobs_table.setAlternatingRowColors(True)
        layout.addWidget(self.jobs_table)

        central_widget.setLayout(layout)

    def search_jobs(self):
        """Fetch jobs and populate the table."""
        search_term = self.search_term_input.text()
        location = self.location_input.text()
        num_pages = self.num_pages_input.text()

        try:
            num_pages = int(num_pages) if num_pages.isdigit() else 1
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Invalid number of pages.")
            return

        jobs_df = fetch_jobs_from_api(search_term, location, num_pages=num_pages)

        if jobs_df.empty:
            QMessageBox.warning(self, "No Results", "No jobs found.")
        else:
            self.populate_table(jobs_df)

    def toggle_map(self):
        """Toggle map visibility."""
        self.map_view.setVisible(not self.map_view.isVisible())

    def populate_table(self, jobs_df):
        """Fill the table with job data."""
        self.jobs_table.setRowCount(len(jobs_df))
        for row_idx, (_, job) in enumerate(jobs_df.iterrows()):
            self.jobs_table.setItem(row_idx, 0, QTableWidgetItem(job.get("job_title", "N/A")))
            self.jobs_table.setItem(row_idx, 1, QTableWidgetItem(job.get("employer_name", "N/A")))
            location = f"{job.get('job_city', 'N/A')}, {job.get('job_state', 'N/A')}"
            self.jobs_table.setItem(row_idx, 2, QTableWidgetItem(location))
            self.jobs_table.setItem(row_idx, 3, QTableWidgetItem(job.get("job_employment_type", "N/A")))
            self.jobs_table.setItem(row_idx, 4, QTableWidgetItem(job.get("job_posted_at_datetime_utc", "N/A")))

            apply_button = QPushButton("Apply")
            apply_button.setIcon(QIcon.fromTheme("link"))
            apply_button.clicked.connect(lambda _, link=job.get("job_apply_link"): webbrowser.open(link))
            self.jobs_table.setCellWidget(row_idx, 5, apply_button)

    def generate_map_html(self):
        """Generate embedded Google Maps HTML."""
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>#map {{ height: 400px; }}</style>
            <script src="https://maps.googleapis.com/maps/api/js?key={GOOGLE_MAPS_API_KEY}"></script>
            <script>function initMap() {{ var map = new google.maps.Map(document.getElementById('map'), {{ center: {{lat: 37.7749, lng: -122.4194}}, zoom: 4 }}); }}</script>
        </head>
        <body onload="initMap()"><div id="map"></div></body>
        </html>
        """

# Main Function
def main():
    app = QApplication(sys.argv)
    load_stylesheet(app)  # Apply QSS here
    window = JobTrackerApp()
    window.show()
    sys.exit(app.exec_())

# Running the app
if __name__ == "__main__":
    main()
