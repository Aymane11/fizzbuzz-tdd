import pytest
from src.utils import ListFactory


def testRange1List():
	factory = ListFactory.create_list(1)
	assert factory == [1]

def testRange3List():
	factory = ListFactory.create_list(3)
	assert factory == [1, 2, 3]

def testRange0List():
	with pytest.raises(ValueError):
		ListFactory.create_list(0)

def testRangeNegativeList():
	with pytest.raises(ValueError):
		ListFactory.create_list(-1)