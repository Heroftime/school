It is a Teacher Directory app created as per techtest document.

This web application is built Django, which is a Python web framework.

Below are the details on how to setup this project.

## Setting up and running the application:

### Check if python is installed
```
python ––version
```

### Install Python (skip this if Python is already installed
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8
python ––version
```

Check here for installation for other OSes: 
https://realpython.com/installing-python/


### Create the virtual environment and activate it
```
python3 -m venv venv

source venv/bin/activate 
```

For Windows only:
Activate the environment:
```
.\venv\Scripts\activate
```

### Install the requirements
```
pip install -r requirements.txt
```

### Migrate the database
```
python manage.py migrate
```

### Create a new superuser
```
python manage.py createsuperuser
```

### Run the server
```
python manage.py runserver
```

## How to use website's functions?

### Navigating the website
- Go to http://localhost:8000/admin
- Login with superuser credentials

### How to run the importer?
- To run the importer, Go to Teachers section -> click on Import or go to http://localhost:8000/admin/teachers/teacher/import/
- Select file to import and Select the format as 'csv'.
- Click on Submit, it will show a preview of all rows that will be imported
    - It will correctly connect all teachers in the system
    - It will create Subjects (if needed) and will correctly linked them to the Teachers.
- Picture profile is connected too.

### On Teachers' section
- All requested functionality is added.
- Only 5 subjects are allowed at a time to a teacher
- Email is unique
- Teach button is there to show the details of the teacher
- The search on the top can be used to search by teachers' last name (first letter or whole last name) and subjects


Please contact me if you face any issues