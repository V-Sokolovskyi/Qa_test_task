import hashlib

def hash_file(filepath, algo):
    h = getattr(hashlib, algo)()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()
