"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var Base62Str = /** @class */ (function () {
    function Base62Str(alphabet) {
        this.alphabet = alphabet;
        this.lookup = this.createLookupTable();
    }
    Base62Str.getBytes = function (str) {
        var bytes = [];
        for (var i = 0; i < str.length; i++) {
            var char = str.charCodeAt(i);
            // tslint:disable-next-line:no-bitwise
            bytes.push(char & 0xFF);
        }
        return bytes;
    };
    Base62Str.getString = function (arr) {
        return String.fromCharCode.apply(this, arr);
    };
    /**
     * Creates a {@link Base62} instance. Defaults to the GMP-style character set.
     *
     * @return a {@link Base62} instance.
     */
    Base62Str.createInstance = function () {
        return this.createInstanceWithGmpCharacterSet();
    };
    /**
     * Creates a {@link Base62} instance using the GMP-style character set.
     *
     * @return a {@link Base62} instance.
     */
    Base62Str.createInstanceWithGmpCharacterSet = function () {
        return new Base62Str(Base62Str.CharacterSets.GMP);
    };
    /**
     * Creates a {@link Base62} instance using the inverted character set.
     *
     * @return a {@link Base62} instance.
     */
    Base62Str.createInstanceWithInvertedCharacterSet = function () {
        return new Base62Str(Base62Str.CharacterSets.INVERTED);
    };
    /**
     * Uses the elements of a byte array as indices to a dictionary and returns the corresponding values
     * in form of a byte array.
     */
    Base62Str.translate = function (indices, dictionary) {
        var translation = [];
        for (var _i = 0, indices_1 = indices; _i < indices_1.length; _i++) {
            var indicesi = indices_1[_i];
            translation.push(dictionary[indicesi]);
        }
        return translation;
    };
    /**
     * Converts a byte array from a source base to a target base using the alphabet.
     */
    Base62Str.convert = function (message, sourceBase, targetBase) {
        /**
         * This algorithm is inspired by: http://codegolf.stackexchange.com/a/21672
         */
        var out = [];
        var source = message;
        while (source.length > 0) {
            var quotient = [];
            var remainder = 0;
            for (var _i = 0, source_1 = source; _i < source_1.length; _i++) {
                var sourcei = source_1[_i];
                // tslint:disable-next-line:no-bitwise
                var accumulator = (sourcei & 0xFF) + remainder * sourceBase;
                var digit = (accumulator - (accumulator % targetBase)) / targetBase;
                remainder = accumulator % targetBase;
                if (quotient.length > 0 || digit > 0) {
                    quotient.push(digit);
                }
            }
            out.push(remainder);
            source = quotient;
        }
        // pad output with zeroes corresponding to the number of leading zeroes in the message
        for (var i = 0; i < message.length - 1 && message[i] === 0; i++) {
            out.push(0);
        }
        return out.reverse();
    };
    /**
     * Encodes a sequence of bytes in Base62 encoding.
     *
     * @param message a byte sequence.
     * @return a sequence of Base62-encoded bytes.
     */
    Base62Str.prototype.encode = function (message) {
        var indices = Base62Str.convert(message, Base62Str.STANDARD_BASE, Base62Str.TARGET_BASE);
        return Base62Str.translate(indices, this.alphabet);
    };
    /**
     * Decodes a sequence of Base62-encoded bytes.
     *
     * @param encoded a sequence of Base62-encoded bytes.
     * @return a byte sequence.
     */
    Base62Str.prototype.decode = function (encoded) {
        var prepared = Base62Str.translate(encoded, this.lookup);
        return Base62Str.convert(prepared, Base62Str.TARGET_BASE, Base62Str.STANDARD_BASE);
    };
    Base62Str.prototype.encodeStr = function (input) {
        return Base62Str.getString(this.encode(Base62Str.getBytes(input)));
    };
    Base62Str.prototype.decodeStr = function (input) {
        return Base62Str.getString(this.decode(Base62Str.getBytes(input)));
    };
    /**
     * Creates the lookup table from character to index of character in character set.
     */
    Base62Str.prototype.createLookupTable = function () {
        var lookup = new Array(256);
        for (var i = 0; i < 256; i++) {
            // tslint:disable-next-line:no-bitwise
            lookup[this.alphabet[i]] = (i & 0xFF);
        }
        return lookup;
    };
    Base62Str.CharacterSets = {
        GMP: [
            '0'.charCodeAt(0), '1'.charCodeAt(0), '2'.charCodeAt(0), '3'.charCodeAt(0), '4'.charCodeAt(0), '5'.charCodeAt(0), '6'.charCodeAt(0), '7'.charCodeAt(0),
            '8'.charCodeAt(0), '9'.charCodeAt(0), 'A'.charCodeAt(0), 'B'.charCodeAt(0), 'C'.charCodeAt(0), 'D'.charCodeAt(0), 'E'.charCodeAt(0), 'F'.charCodeAt(0),
            'G'.charCodeAt(0), 'H'.charCodeAt(0), 'I'.charCodeAt(0), 'J'.charCodeAt(0), 'K'.charCodeAt(0), 'L'.charCodeAt(0), 'M'.charCodeAt(0), 'N'.charCodeAt(0),
            'O'.charCodeAt(0), 'P'.charCodeAt(0), 'Q'.charCodeAt(0), 'R'.charCodeAt(0), 'S'.charCodeAt(0), 'T'.charCodeAt(0), 'U'.charCodeAt(0), 'V'.charCodeAt(0),
            'W'.charCodeAt(0), 'X'.charCodeAt(0), 'Y'.charCodeAt(0), 'Z'.charCodeAt(0), 'a'.charCodeAt(0), 'b'.charCodeAt(0), 'c'.charCodeAt(0), 'd'.charCodeAt(0),
            'e'.charCodeAt(0), 'f'.charCodeAt(0), 'g'.charCodeAt(0), 'h'.charCodeAt(0), 'i'.charCodeAt(0), 'j'.charCodeAt(0), 'k'.charCodeAt(0), 'l'.charCodeAt(0),
            'm'.charCodeAt(0), 'n'.charCodeAt(0), 'o'.charCodeAt(0), 'p'.charCodeAt(0), 'q'.charCodeAt(0), 'r'.charCodeAt(0), 's'.charCodeAt(0), 't'.charCodeAt(0),
            'u'.charCodeAt(0), 'v'.charCodeAt(0), 'w'.charCodeAt(0), 'x'.charCodeAt(0), 'y'.charCodeAt(0), 'z'.charCodeAt(0)
        ],
        INVERTED: [
            '0'.charCodeAt(0), '1'.charCodeAt(0), '2'.charCodeAt(0), '3'.charCodeAt(0), '4'.charCodeAt(0), '5'.charCodeAt(0), '6'.charCodeAt(0), '7'.charCodeAt(0),
            '8'.charCodeAt(0), '9'.charCodeAt(0), 'a'.charCodeAt(0), 'b'.charCodeAt(0), 'c'.charCodeAt(0), 'd'.charCodeAt(0), 'e'.charCodeAt(0), 'f'.charCodeAt(0),
            'g'.charCodeAt(0), 'h'.charCodeAt(0), 'i'.charCodeAt(0), 'j'.charCodeAt(0), 'k'.charCodeAt(0), 'l'.charCodeAt(0), 'm'.charCodeAt(0), 'n'.charCodeAt(0),
            'o'.charCodeAt(0), 'p'.charCodeAt(0), 'q'.charCodeAt(0), 'r'.charCodeAt(0), 's'.charCodeAt(0), 't'.charCodeAt(0), 'u'.charCodeAt(0), 'v'.charCodeAt(0),
            'w'.charCodeAt(0), 'x'.charCodeAt(0), 'y'.charCodeAt(0), 'z'.charCodeAt(0), 'A'.charCodeAt(0), 'B'.charCodeAt(0), 'C'.charCodeAt(0), 'D'.charCodeAt(0),
            'E'.charCodeAt(0), 'F'.charCodeAt(0), 'G'.charCodeAt(0), 'H'.charCodeAt(0), 'I'.charCodeAt(0), 'J'.charCodeAt(0), 'K'.charCodeAt(0), 'L'.charCodeAt(0),
            'M'.charCodeAt(0), 'N'.charCodeAt(0), 'O'.charCodeAt(0), 'P'.charCodeAt(0), 'Q'.charCodeAt(0), 'R'.charCodeAt(0), 'S'.charCodeAt(0), 'T'.charCodeAt(0),
            'U'.charCodeAt(0), 'V'.charCodeAt(0), 'W'.charCodeAt(0), 'X'.charCodeAt(0), 'Y'.charCodeAt(0), 'Z'.charCodeAt(0)
        ]
    };
    Base62Str.STANDARD_BASE = 256;
    Base62Str.TARGET_BASE = 62;
    return Base62Str;
}());
const base62 = Base62Str.createInstance();
const decodedString = base62.decodeStr(process.argv[2]);
console.log(decodedString);
// node index.js T8dgcjRGkZ3aysdN // hellworld !