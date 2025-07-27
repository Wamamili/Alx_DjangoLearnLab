# Permissions and Groups Setup

## Custom Permissions (Defined in Book model)
- can_view: Can view book entries
- can_create: Can add new books
- can_edit: Can update existing books
- can_delete: Can remove books from the system

## Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: Full access

## Setup Steps
1. Go to Admin > Groups > Add
2. Assign permissions to each group accordingly
3. Assign users to the relevant groups
4. Views are protected using @permission_required
