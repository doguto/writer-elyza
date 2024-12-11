import sys
sys.path.append('../')
from web_operation_py.alphapolis_operater import AlphapolisOperaterPy

def test():
    operater = AlphapolisOperaterPy()
    operater.login()


if __name__ == '__main__':
    test()