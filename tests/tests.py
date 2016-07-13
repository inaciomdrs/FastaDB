# TODO - Simple tests for checking the code verasity
# TODO - Make the tests run on Jenkins environment
# import os
# import unittest
from FastaDB.FastaDB import FastaDB


def CreateDB(self):
	cursor = fdb()
	cursor.DB("new-db.fdb")
