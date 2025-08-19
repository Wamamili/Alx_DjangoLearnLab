### Running API Tests
The API has unit tests for CRUD, filtering, searching, ordering, and permissions.

Run tests:
    python manage.py test api

Examples:
- Create Book: POST /api/books/
- Filter Books: GET /api/books/?author=Author A
- Search Books: GET /api/books/?search=Book One
- Order Books: GET /api/books/?ordering=publication_year
