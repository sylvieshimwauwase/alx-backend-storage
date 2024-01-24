#!/usr/bin/env/python3
"""performing reddis functions"""

import redis
import uuid
from typing import Callable
from functools import wraps


class Cache:
    def __init__(self, host='localhost', port=6379, db=0):
        """
        Initialize cache class
        param host: redis server
        param db: redis server port
        """

        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()


    def store(self, data: str) -> str:
        """store data in redis
        param data: data to be stored
        return: generated key
        """

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    
    def get(self, key: str) -> str:
        """
        Retrieve data from Redis .
        param key: The key associated with the stored data.
        param fn: A callable function to convert the retrieved data.
        return: The retrieved data with optional conversion.
        """
        
        return self._redis.get(key).decode("utf-8")
    
    def get_str(self, key: str) -> str:
        """
        Retrieve string data from Redis 
        param key: The key associated with the stored string data.
        return: The retrieved string data.
        """

        return self.get(key)

    def get_int(self, key: str) -> int:
        """
        Retrieve integer data from Redis
        param key: The key associated with the stored integer data.
        return: The retrieved integer data.
        """

        return int(self.get(key))

def call_history(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method is called.

    :param method: The method to be decorated.
    :return: The decorated method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = method.__qualname__ + ":inputs"
        outputs_key = method.__qualname__ + ":outputs"
        self._redis.rpush(inputs_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(output))

        return output
    
    return wrapper
        