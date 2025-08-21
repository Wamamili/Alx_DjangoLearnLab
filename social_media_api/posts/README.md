# Posts and Comments API

## Endpoints
- GET /api/posts/ (list, search, paginated)
- POST /api/posts/ (create)
- GET /api/posts/{id}/ (retrieve)
- PUT /api/posts/{id}/ (update - owner only)
- DELETE /api/posts/{id}/ (delete - owner only)

- GET /api/comments/
- POST /api/comments/
- PUT /api/comments/{id}/ (owner only)
- DELETE /api/comments/{id}/ (owner only)

## Auth
Use "Authorization: Token <token>" in headers.
