# Utils for the runnable tutorials on python
# Made by http://www.elmalabarista.com


def printTitle(text):
    print ''
    print '*' * len(text)
    print str.upper(text)
    print '*' * len(text)
    print ''


def printSubTitle(text):
    print ''
    print str.upper(text)
    print '=' * len(text)
    print ''


def printExplain(text):
    print ''
    print text
    print '-' * len(text)
    print ''


def printEqual(left, compare, rigth):
    print left, compare, rigth


def printTab(text):
    print '\t', text
