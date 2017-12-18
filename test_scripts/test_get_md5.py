import hashlib


def get_md5_hash():
    _api_key = '00000000-0000-0000-0000-000000000000'
    _secret = '1234567890ABCDEF'
    _routing_id = '1464524676'

    routing_key_data = str(_api_key) + str(_routing_id) + str(_secret)
    digest_string = hashlib.md5(routing_key_data.encode('utf-8')).hexdigest()
    print("Digest string " + digest_string)

if __name__ == '__main__':
    get_md5_hash()
