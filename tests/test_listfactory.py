from src.utils import ListFactory


def testRange1List():
	factory = ListFactory.create_list(1)
	assert factory == [1]

def testRange3List():
	factory = ListFactory.create_list(3)
	assert factory == [1, 2, 3]