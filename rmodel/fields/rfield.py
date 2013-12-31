# coding: utf8
from rmodel.fields.base_field import BaseField


class rfield(BaseField):

    def assign(self, inst):
        self.key = inst.cursor.key
        self.instance = inst
        self.cursor = inst.cursor.new(self.prefix)

    def clean(self, pipe):
        pipe.hdel(self.key, self.prefix)
#        self._session.add(self.cursor.items, None)

    def collect_data(self, pipe):
        return pipe.hget(self.key, self.prefix)

    def set(self, value):
        self._session.add(self.cursor.items, value)
        return self.redis.hset(self.key, self.prefix,
                               self.onsave(value))

    def get(self):
        return self.process_result(self.collect_data(self.redis))

    def onincr(self, value):
        return value

    def _incr(self, redis, value):
        return redis.hincrby(self.key, self.prefix, value)

    def incr(self, value):
        self.set(self.get() + value)
        self._session.add(self.cursor.items, value)
        return value

    def __isub__(self, value):
        self.incr(-value)
        return self

    def __iadd__(self, value):
        self.incr(value)
        return self
