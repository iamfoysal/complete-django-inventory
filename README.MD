# Django Inventory Management System


This is a simple inventory management system built with Django. It allows users to add, update, and delete products from the inventory. It also allows users to upload multiple files to the server.

## Screenshots
![Login page](/site-image/Sign-In.png)

![Product page](/site-image/Inventory-Management.png)


"""
This code is part of a locally run Django project.

To run the project locally, follow these steps:

1. Install Python and Django on your machine.
2. Clone the project repository from GitHub.
3. Create a virtual environment and activate it.
4. Install the project dependencies using pip.
5. Set up the database by running migrations.
6. Start the development server using the 'manage.py' script.


Note: Make sure to update the settings file with the necessary configurations for your local environment.
"""


## Features

- Login and registration system
- Add, update, and delete products(stock management, price, and quantity)
- View product details
- Product search
- Product Categories
- Image download
- Upload multiple files
- Email Sending
- RESTful API for product management
- File upload API
- Docker support


## Technologies
- Python
- Django
- SQLite/PostgreSQL/MySQL
- HTML
- CSS
- JavaScript
- Docker
- Django Rest Framework



## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/iamfoysal/complete-django-inventory
    ```
2. Navigate to the project directory:

   ```bash
   cd complete-django-inventory
   ```
3. Create a virtual environment:

   ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```
5. Install the project dependencies:

   ```bash
    pip install -r requirements.txt
    ```
6. Run the migrations:

   ```bash
    python manage.py migrate
    ```
7. Start the development server:

   ```bash
    python manage.py runserver
    ```
8. Open the following URL in your browser:

   ```
   http://localhost:8000
   ```

[API docs](/API_INFO.MD)


##### if you want to run the project in your local machine using docker then follow the below steps:

1. After clone the repository, navigate to the project directory:

   ```bash
   cd complete-django-inventory
   ```
2. Run the following command to build the docker image:

   ```bash
    docker-compose build
    ```

3. Run the following command to start the docker container:

   ```bash
    docker-compose up
    ```

4. Open the following URL in your browser:

   ```
   http://localhost:8000
   ```



### Contributions are always welcome! If you want to contribute to this project:

1. 🍴 Fork the project.
2. 🔨 Create your feature branch (`git checkout -b my-new-feature`).
3. 💻 Make your changes.
4. ✅ Ensure the tests pass and the code is linted (`black . && pytest`).
5. 📝 Write or update tests for the changes that you made.
6. 📝 Write a good commit message.
7. 🌟 Push to the branch (`git push origin my-new-feature`).
8. 🔃 Create a new Pull Request.

Thank you for your contributions!


