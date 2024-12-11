import sys
sys.path.append('../')
# from src.writer.writer import Writer
from writer.writer import Writer

def test():

    writer = Writer()
    writer.save_test_story(title='test2',story_number=2,text='hogehogehoge\nfugafuga')


if __name__ == '__main__':
    test()