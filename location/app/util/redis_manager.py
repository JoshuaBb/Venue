"""Module created as a wrapper around Redis Cache and is responsible for creating the cache"""
import os
import redis


class RedisManager:
    """Class that wraps Redis functionality"""
    def __init__(self, name_space: str):
        redis_host = os.getenv('REDIS_HOST')
        redis_port = int(os.getenv('REDIS_PORT'))

        self.name_space = name_space
        self.redis = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

    def adjusted_key(self, key):
        """Adds a namespace identifier to the redis cache to make it easier to identify keys"""
        return f"{self.name_space}_{key}"

    async def get(self, key: str):
        """Pass through get method to retrieve a value from a redis cache"""
        value = self.redis.get(self.adjusted_key(key))
        return value

    async def set(self, key: str, value: str):
        """Set the value of key for a redis cache"""
        value = self.redis.set(self.adjusted_key(key), value)
        return value

    async def delete(self, key):
        """Deletes a key from a redis cache"""
        return self.redis.delete(self.adjusted_key(key))
