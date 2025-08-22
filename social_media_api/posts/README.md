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
# Follow & Feed

## Endpoints
- POST /api/accounts/follow/<user_id>/  (auth required)
- POST /api/accounts/unfollow/<user_id>/  (auth required)
- GET /api/feed/  (auth required) → returns posts from followed users

## Notes
- Users cannot follow/unfollow themselves
- Feed ordered by newest posts
