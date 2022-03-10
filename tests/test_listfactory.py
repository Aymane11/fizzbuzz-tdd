from src.utils import ListFactory


def testOneItemList():
	factory = ListFactory.create_list(1)
	assert factory == [1]