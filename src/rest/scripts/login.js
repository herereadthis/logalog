const execSync = require('child_process').execSync;

const output = execSync(
    'curl -d \'{"email": "foo@bar.com", "password": "123"}\' -H "Content-Type: application/json" -X POST http://localhost:3001/api/auth',
    { encoding: 'utf-8' }
);

console.log(output);