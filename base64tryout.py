import base64 as b64

_a = b64.b64decode
_p = "cHJpbnQoJ0hlbGxvIFdvcmxkJyk="

exec(_a(_p).decode())