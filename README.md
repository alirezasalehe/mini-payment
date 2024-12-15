## Development

Run tests: `./manage.py test`

Run server: `./manage.py runserver`

You can use this curl to test transactions list API:

```
curl -X GET -H "Content-Type: application/json" http://localhost:8000/transactions/?phone_number=<phone_number>
```
