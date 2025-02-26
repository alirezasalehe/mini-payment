A very simple app to manage transactions of users.

### Useful Commands

- `python manage.py test`

- `python manage.py runserver` (before running server you may need to install requirements: `pip install -r requirements.txt` and migrate database: `python manage.py migrate`)

- `python manage.py populate_db` (to populate database with some data)

### APIs

You can use this curl to test transactions list API:

```bash
curl -X GET -H "Content-Type: application/json" "http://localhost:8000/transactions/?phone_number=<phone_number>"
```
