// buuoj equation

const s = 'l[!+[]+!+[]+!+[]+!+[]+[+[]]]+l[!+[]]&&l[!+[]+!+[]+!+[]+[+!+[]]]+l[!+[]+!+[]+!+[]+[!+[]+!+[]+!+[]+!+[]+!+[]]]==81'
const decode = str => {
	for(let i=0;i<=1;i++){
		str = str.replace(/l\[(\D*?)](\+l|-l|==)/g,  (m,a,b) => `l[${eval(a)}${b}]`);
		str = str.replace(/==(\D*?)&&/g,  (m,a) => `==${eval(a)}&&`);
	}
	return str;
}
ss = decode(s);
console.log(ss)