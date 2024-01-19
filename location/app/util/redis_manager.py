import redis
class RedisManager:
    def __init__(self, host: str, port: int):
        self.redis = redis.Redis(host=host, port=port, decode_responses=True)

    async def get(self, key: str):
        value = self.redis.get(key)
        return value

    async def set(self, key: str, value: str):
        value = self.redis.set(key, value)
        return value

    async def delete(self, key):
        return self.redis.delete(key)


