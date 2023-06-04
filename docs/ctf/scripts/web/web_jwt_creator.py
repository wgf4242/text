import base64, hashlib, hmac, json, secrets


def base64url_decode(input):
    return base64.urlsafe_b64decode(input + '==')


def base64url_encode(input):
    string_as_bytes = input.replace(b' ', b'')
    string_as_base64 = base64.urlsafe_b64encode(string_as_bytes).replace(b'=', b'')
    return string_as_base64


def encode(header):
    msg = json.dumps(header, separators=(',', ':'))
    msg = msg.encode()
    return base64url_encode(msg)


def jwt_creator():
    header = {"alg": "HS256", "typ": "JWT"}
    payload = {"username": "admin"}
    secret_key = '1Kun'  # secrets.token_urlsafe(32)
    msg = encode(header) + b'.' + encode(payload)
    signature = hmac.new(secret_key.encode(), msg, hashlib.sha256).digest()
    return b'.'.join([msg, base64url_encode(signature)])


if __name__ == '__main__':
    token = jwt_creator()
    print(token)
