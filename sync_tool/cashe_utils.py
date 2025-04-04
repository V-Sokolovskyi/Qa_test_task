import os
import json

class Cashe():

    def __init__(self,cache_file_name = "hash_cache.json"):
        self.cache_file = cache_file_name
        self.hash_cache =self._load_cashe()

    def _load_cashe(self):
        if os.path.exists(self.cache_file):
            with open(self.cache_file, 'r') as f:
                self.hash_cache = json.load(f)
                print("Loaded hash cache from file.")
        else:
            print("Initialized empty hash cache.")
        return {}

    def save_cache(self):
        with open(self.cache_file, 'w') as f:
            json.dump(self.hash_cache, f, indent = 4)
            print("Saved hash cache to file.")

    def clean_cashe(self):
        keys_to_delete = [path for path in self.hash_cache if not os.path.exists(path)]
        for key in keys_to_delete:
            del self.hash_cache[key]
            print(f"Removed stale cache entry: {key}")