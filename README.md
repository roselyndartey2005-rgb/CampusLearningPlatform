 Campus Learning Resource Platform
 About
The Campus Learning Resource Platform is a backend application built with Django and Django REST Framework. It provides a structured way to manage academic courses and their learning materials, making resources easier to organise and retrieve.

 Technologies
- Python
- Django
- Django REST Framework
- SQLite

 Features
- Course management (Create, Read, Update and Delete).
- Learning resource management (Create, Read, Update and Delete).
- Organisation of resources by course.
- Support for notes, videos and external links.
- Retrieval of resources belonging to a specific course.
- Resource counting for each course.
- API pagination.

 API Endpoints

| Endpoint | Description |
|---|---|
| `/api/courses/` | Manage courses |
| `/api/resources/` | Manage learning resources |
| `/api/courses/<id>/resources/` | Retrieve course resources |
| `/api/courses/resource-counts/` | View resource counts |

