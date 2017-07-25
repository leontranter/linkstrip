import unittest
import strip


class TestLinks(unittest.TestCase):
    def test_can_create_a_link(self):
        testString = r"http://abc.com/someurl" + "\n"
        expectedString = r"Someurl: http://abc.com/someurl #test" + "\n"
        outputString  = strip.modifyLink(testString, "#test")
        self.assertEqual(expectedString, outputString)

    def test_can_strip_a_link(self):
    	testString = r"http://abc.com/someurl?utm_source=Iterable" + "\n"
    	expectedString = r"Someurl: http://abc.com/someurl #test" + "\n"
    	outputString = strip.modifyLink(testString, "#test")
    	self.assertEqual(expectedString, outputString)

    def test_can_strip_hyphens(self):
    	testString = r"http://abc.com/someurl/name-of-article" + "\n"
    	expectedString = r"Name of article: http://abc.com/someurl/name-of-article #test" + "\n"
    	outputString = strip.modifyLink(testString, "#test")
    	self.assertEqual(expectedString, outputString)

    def test_can_strip_underscores(self):
    	testString = r"http://abc.com/someurl/name_of_article" + "\n"
    	expectedString = r"Name of article: http://abc.com/someurl/name_of_article #test" + "\n"
    	outputString = strip.modifyLink(testString, "#test")
    	self.assertEqual(expectedString, outputString)


if __name__ == "__main__":
	unittest.main()