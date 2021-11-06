REST

```bash
npm start

curl -d '{"email": "foo@bar.com", "password": "123"}' -H "Content-Type: application/json" -X POST http://localhost:3001/api/auth
curl -H "Content-Type: application/json" -H "x-auth-token: <JWTOKEN>" -X GET http://localhost:3001/api/messages
```
