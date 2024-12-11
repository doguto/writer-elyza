import sys
sys.path.append('../')
# from src.writer.writer import Writer
from writer.writer import Writer

def test():

    writer = Writer()
    writer.save_story(title='test',story_number=1,text='hogehoge\nfugafuga')


if __name__ == '__main__':
    test()