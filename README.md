# File Copy Restriction

This project is a Django application designed to manage and configure a root folder for file restrictions. It provides a simple interface for configuring the root folder path, and checks the configuration status.

## Features

- Configure the root folder for file copying restrictions.
- View configuration settings.
- Redirect to a confirmation page after saving configuration.

## Setup Instructions

### Prerequisites

- Python 3.x
- Django 3.x or above
- SQLite (or other database systems, based on your configuration)

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/file_copy_restriction.git
   
2. Navigate to the project directory:
   ```bash
   cd file_copy_restriction

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

4. Apply the migrations to set up the database:
   ```bash
   python manage.py migrate

5. Run the development server:
   ```bash
   python manage.py runserver

6. Access the app in your browser at http://127.0.0.1:8000/.
    ### URL Routes
   - /filemonitor/configure/: View and update the root folder configuration.
   - /filemonitor/somewhere/: Confirmation page showing the success message.

### Testing
7. To run the tests for this project, execute:
   ```bash
   python manage.py test

   



