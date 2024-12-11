import sys
sys.path.append('../')
from web_operation.alphapolis_operater import AlphapolisOperater

def test():
    operater = AlphapolisOperater()
    operater.login()


if __name__ == '__main__':
    test()