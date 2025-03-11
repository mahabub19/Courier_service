# Courier Service API

## Setup Instructions

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Start the server: `python manage.py runserver`

## API Endpoints

- `GET /api/packages/`: List all packages.
- `POST /api/packages/`: Create a new package.
- `GET /api/packages/<id>/`: Retrieve a package.
- `PUT /api/packages/<id>/`: Update a package.
- `DELETE /api/packages/<id>/`: Soft delete a package.
