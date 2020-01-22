 ## Django REST API
 ### Restaurant example

 #### Getting started

 1. Have python3 installed
 2. Initialize a new virtual environment: python3 -m venv env
 3. Activate your virtual env: source venv/bin/activate
  4. Intall the project dependencies: pip install -r requirements.txt
 5. Install postgres, create a DB and replace the configurations in Django settings.
 6. Got inside the project directory.
 7. Apply migrations: python3 manage.py migrate
 8. Create superuser : python3 manage.py createsuperuser
 8. Start the local server: python3 manage.py runserver

 #### ENDPOINTS

 * **GET, POST:**  /restaurants
 * **GET, DELETE:** /restaurants/<str:restaurant_id>
 * **GET, POST:** /restaurants/<str:restaurant_id>/recipes
 * **GET, DELETE:** /restaurants/<str:restaurant_id>/recipes/<str:recipe_id>
