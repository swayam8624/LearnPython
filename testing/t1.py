# pylint
# pyflakes
# pep8

# how to do even more?
import unittest  # look into documentation for more
import m1  # hypothetically we have many functions


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        print("about to test")

    def test_do_stuff(self):
        testparam = 10
        result = m1.do_stuff(testparam)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        testparam = 'sty'
        result = m1.do_stuff(testparam)
        self.assertTrue(isinstance(result, ValueError))  # error raised is an instance of ValueError class
        # or assertIsInstance

    def test_do_stuff3(self):
        testparam = None
        result = m1.do_stuff(testparam)
        self.assertEqual(result, "please enter a num")

    def test_do_stuff4(self):
        testparam = ''
        result = m1.do_stuff(testparam)
        self.assertEqual(result, "please enter a num")

    def tearDown(self) -> None:
        print("cleaning up")


# setup and teardown is called immediately before and after each test

if __name__ == '__main__':
    unittest.main()

# terminal tips:
'''
on terminal if we type 
python3 -m unittest ,
it runs all the test files with unittest module simultaneously

if we type 
python -m unittest -v ,
it gives more detailed view of which test failed and which succeeded
'''
