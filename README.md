"# job_scraper" 
A web application that scrapes Python developer job listings from Indeed.com and provides salary analysis.
Features

Web scraping of Indeed.com job listings
MongoDB database storage
Django admin panel for job management
Salary analysis using NumPy and Pandas
Interactive web interface

Setup Instructions

Clone the repository

bashCopygit clone https://github.com/YOUR_USERNAME/python-job-scraper.git
cd python-job-scraper

Create virtual environment

bashCopypython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies

bashCopypip install -r requirements.txt

Set up environment variables
Create a .env file with:

CopyMONGODB_URI=your_mongodb_uri
SECRET_KEY=your_django_secret_key

Run migrations

bashCopypython manage.py migrate

Create superuser

bashCopypython manage.py createsuperuser

Run the application

bashCopypython manage.py runserver
Deployment
The application is deployed on Heroku at: https://python-jobs-dashboard.herokuapp.com
Analysis Notebook
The salary analysis notebook is available in the analysis folder.
