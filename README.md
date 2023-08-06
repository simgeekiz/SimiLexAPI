# SimiLex API 


## Installation for Python development

1. Clone the repository
    ```shell
    $ python3 -m venv .env
    ```
2. Create a virtual environment and then activate it
    ```shell
    $ python3 -m venv .env
    $ source .env/bin/activate
    ```

3. Install requirements.txt (I do not want to create requirements.txt)
    ```shell
    $ pip install jupyter
    $ pip install gensim
    $ pip install flask
    $ pip install gunicorn
    ```

4. Run the api 
      ```shell
    $ python api.py
    or
    $ gunicorn api:app
    ```

# Licence 
    MIT License: http://igliu.mit-license.org/
