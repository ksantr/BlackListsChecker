from blcheck.blcheck import BlackListsChecker

def test_b():
    sp = BlackListsChecker(threads=20)
    result = sp.is_spam('github.com')

