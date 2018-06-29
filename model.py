#!/usr/bin/env python3

import os
from peewee import Model, CharField, DecimalField, ForeignKeyField
from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))

class Donor(Model):
    name = CharField(max_length=255, unique=True)

    class Meta:
        database = db


class Donation(Model):
    donor = ForeignKeyField(Donor, related_name='donated_by', null=False)
    value = DecimalField(max_digits = 10, decimal_places = 2)

    class Meta:
        database = db

if __name__ == "__main__":
    pass
