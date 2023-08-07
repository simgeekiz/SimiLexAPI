# SimiLex API 

### Installation
Follow these steps to install and run the project on your local machine.

### Prerequisites

- Python 3.x (Install from [python.org](https://www.python.org/downloads/))
- Git (Install from [git-scm.com](https://git-scm.com/downloads))

### Clone the Repository

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command to clone the repository:

  ```bash
  $ git clone https://github.com/simgeekiz/SimiLexAPI.git
  ```

### Set Up Virtual Environment (Optional but Recommended)

1. Navigate to the project directory:

  ```bash
  $ cd your-repo
  ```

2. Create a virtual environment and then activate it;

  - On macOS and Linux:
  ```bash
  $ python3 -m venv .env
  $ source .env/bin/activate
  ```

  - On Windows:
  ```bash
  $ python -m venv .env
  $ .\.env\Scripts\activate
  ```

### Install Dependencies

If there is no requirements.txt
  ```bash
  $ pip install jupyter
  $ pip install gensim
  $ pip install flask
  $ pip install gunicorn
  ```
or 

  ```bash
  $ pip install -r requirements.txt
  ``` 


### Run the API 
1. Start the Flask application:
```bash
$ python api.py
or
$ gunicorn api:app
```

2. Open your web browser and navigate to http://localhost:5000 to access the application. If you use gunicorn navigate to http://localhost:8000

### Deactivate Virtual Environment

When you're done using the project, deactivate the virtual environment:
  ```bash
  deactivate
  ```

### Prepare a Flask application for Heroku
1. Create the Procfile
  ```bash
    web: gunicorn api:app
  ```
  
2. Create the requirements.txt 
  Heroku needs requirements.txt to understand that it is a python app
  
  ```bash
    pip freeze > requirements.txt
  ```

### Set up Heroku

1. Install Heroku CLI and the login via terminal(for linux).

  ```bash
    heroku login
  ```

2. Create a Heroku app

  ```bash
    heroku create similexapi
  ```

3. Create the runtime.txt
Specify the python version
  ```bash
    python-3.10.6
  ```
### Build a CI/CD pipeline with GitHub Actions

After pushing the code to the repository, the CI/CD pipeline will automatically initiate.

Do not forget to add your private variables into secrets
e.g. secrets.HEROKU_API_KEY

# Licence 
  MIT License: http://igliu.mit-license.org/
