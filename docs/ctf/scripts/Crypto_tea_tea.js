/******************************************

Use: "Hello World!".encrypt("key")
	=> "íSjÝqTÂWÕãAa[UÄ"
******************************************/
String.prototype.encrypt = function(password) {
	const v = new Array(2);
	const k = new Array(4);
	let s = "";
	var i;

	plaintext = escape(this); // use escape() so only have single-byte chars to encode

	// build key directly from 1st 16 chars of password
	for (var i = 0; i < 4; i++) k[i] = Str4ToLong(password.slice(i * 4, (i + 1) * 4));

	for (i = 0; i < plaintext.length; i += 8) { // encode plaintext into s in 64-bit (8 char) blocks
		v[0] = Str4ToLong(plaintext.slice(i, i + 4)); // ... note this is 'electronic codebook' mode
		v[1] = Str4ToLong(plaintext.slice(i + 4, i + 8));
		code(v, k);
		s += LongToStr4(v[0]) + LongToStr4(v[1]);
	}

	return escCtrlCh(s);
	// note: if plaintext or password are passed as string objects, rather than strings, this
	// function will throw an 'Object doesn't support this property or method' error
}

// Like C code

function code(v, k) {
    // Extended TEA: this is the 1997 revised version of Needham & Wheeler's algorithm
    // params: v[2] 64-bit value block; k[4] 128-bit key
    let y = v[0];

    let z = v[1];
    const delta = 0x9E3779B9;
    const limit = delta * 32;
    let sum = 0;

    while (sum != limit) {
		y += (z << 4 ^ z >>> 5) + z ^ sum + k[sum & 3];
		sum += delta;
		z += (y << 4 ^ y >>> 5) + y ^ sum + k[sum >>> 11 & 3];
		// note: unsigned right-shift '>>>' is used in place of original '>>', due to lack
		// of 'unsigned' type declaration in JavaScript (thanks to Karsten Kraus for this)
	}
    v[0] = y;
    v[1] = z;
}

// supporting functions

function Str4ToLong(s) { // convert 4 chars of s to a numeric long
	let v = 0;
	for (let i = 0; i < 4; i++) v |= s.charCodeAt(i) << i * 8;
	return isNaN(v) ? 0 : v;
}

function LongToStr4(v) { // convert a numeric long to 4 char string
	const s = String.fromCharCode(v & 0xFF, v >> 8 & 0xFF, v >> 16 & 0xFF, v >> 24 & 0xFF);
	return s;
}

function escCtrlCh(str) { // escape control chars which might cause problems with encrypted texts
	return str.replace(/[\0\t\n\v\f\r\xa0'"!]/g, c => `!${c.charCodeAt(0)}!`);
}

function unescCtrlCh(str) { // unescape potentially problematic nulls and control characters
	return str.replace(/!\d\d?\d?!/g, c => String.fromCharCode(c.slice(1, -1)));
}

// module.exports = (text, password) => text.encrypt(password);

/******************************************
Use: "íSjÝqTÂWÕãAa[UÄ".decrypt("key")
	=> "Hello World!"
******************************************/
String.prototype.decrypt = function(password) {
    const v = new Array(2);
    const k = new Array(4);
    let s = "";
    var i;

    for (var i = 0; i < 4; i++) k[i] = Str4ToLong(password.slice(i * 4, (i + 1) * 4));

    ciphertext = unescCtrlCh(this);
    for (i = 0; i < ciphertext.length; i += 8) { // decode ciphertext into s in 64-bit (8 char) blocks
    v[0] = Str4ToLong(ciphertext.slice(i, i + 4));
    v[1] = Str4ToLong(ciphertext.slice(i + 4, i + 8));
    decode(v, k);
    s += LongToStr4(v[0]) + LongToStr4(v[1]);
  }

    // strip trailing null chars resulting from filling 4-char blocks:
    s = s.replace(/\0+$/, '');

    return unescape(s);
};
// Like C code

function decode(v, k) {
    let y = v[0];
    let z = v[1];
    const delta = 0x9E3779B9;
    let sum = delta * 32;

    while (sum != 0) {
    z -= (y << 4 ^ y >>> 5) + y ^ sum + k[sum >>> 11 & 3];
    sum -= delta;
    y -= (z << 4 ^ z >>> 5) + z ^ sum + k[sum & 3];
  }
    v[0] = y;
    v[1] = z;
}


// supporting functions

function Str4ToLong(s) { // convert 4 chars of s to a numeric long
  let v = 0;
  for (let i = 0; i < 4; i++) v |= s.charCodeAt(i) << i * 8;
  return isNaN(v) ? 0 : v;
}

function LongToStr4(v) { // convert a numeric long to 4 char string
  const s = String.fromCharCode(v & 0xFF, v >> 8 & 0xFF, v >> 16 & 0xFF, v >> 24 & 0xFF);
  return s;
}

function escCtrlCh(str) { // escape control chars which might cause problems with encrypted texts
  return str.replace(/[\0\t\n\v\f\r\xa0'"!]/g, c => `!${c.charCodeAt(0)}!`);
}

function unescCtrlCh(str) { // unescape potentially problematic nulls and control characters
  return str.replace(/!\d\d?\d?!/g, c => String.fromCharCode(c.slice(1, -1)));
}

// module.exports = (text, password) => text.decrypt(password);
