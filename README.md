# Resume Uploader and Analyzer

This Django-based project facilitates resume uploading, stores candidate information, and offers features for analyzing resume content. Additionally, an 'About Us' section is included to provide information about the project and its creators.

## Installation Requirements

- Ensure Python and Django are installed.
- Set up a virtual environment (optional but recommended).

## Database Setup

- Configure your database in the `settings.py` file (sqlite3 is used in this example).

## Project Setup

1. Clone or download the project files.
2. Navigate to the project directory.
3. Run migrations: `python manage.py makemigrations` and `python manage.py migrate`.

## Running the Server

- Start the Django development server: `python manage.py runserver`.
- Access the application in a web browser at `http://127.0.0.1:8000/`.

## Views Description

### HomeView

- Renders the home page for resume uploading and displays existing candidate details.

### CandidateView

- Displays detailed information about a specific candidate.

### ResumeAnalysisView

- Analyzes resume content by generating a bar chart of the top 10 most frequent words. Categorizes resumes based on the most frequent word found, defining professional domains.

### AboutUsView

- Renders the 'About Us' page to provide an overview of the project.

## Usage

1. Access the homepage to upload resumes and view existing candidate details.
2. Navigate to the 'About Us' section for project information.
3. Explore the 'Resume Analysis' section to visualize word frequency and categorize resumes based on profession.

## Dependencies

- Python
- Django
- NLTK
- Matplotlib
- Seaborn

Further, refer to requirements.txt for installing all the required dependencies.
