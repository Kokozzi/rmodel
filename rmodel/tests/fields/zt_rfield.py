#coding: utf8
from rmodel.fields.rfield import rfield
from rmodel.tests.base_test import BaseTest


class RfieldTest(BaseTest):

    def setUp(self):
        super(RfieldTest, self).setUp()
        self.unbound = rfield(int, 0)
        self.unbound.bound(self.model, 'field')

    def test_init(self):
        self.eq(self.model.field.get(), 0)

    def test_cursor(self):
        self.eq(self.model.field.cursor.items, ('model', 'field'))

    def test_incr(self):
        self.model.field -= 10
        self.eq(self.model.field.get(), -10)

    def test_default_int(self):
        self.unbound2 = rfield(int, 10)
        self.unbound2.bound(self.model, 'field2')
        self.eq(self.model.field2.get(), 10)
        self.model.field2 += 10
        self.eq(self.model.field2.get(), 20)
        self.model.field2 -= 12
        self.eq(self.model.field2.get(), 8)