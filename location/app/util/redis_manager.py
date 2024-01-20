import redis
import os

class RedisManager:
    def __init__(self):
        redis_host = os.getenv('REDIS_HOST')
        redis_port = int(os.getenv('REDIS_PORT'))

        self.redis = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

    async def get(self, key: str):
        value = self.redis.get(key)
        return value

    async def set(self, key: str, value: str):
        value = self.redis.set(key, value)
        return value

    async def delete(self, key):
        return self.redis.delete(key)


