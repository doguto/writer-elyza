import time
import sys
sys.path.append('../')
from writer.writer import Writer
from writer.elyza import Elyza

def test():
    writer = Writer()
    elyza = Elyza()
    
    start = time.time()
    title = elyza.generate_title()
    print(time.time() - start)
    print(title)
    
    # writer.save_test_story(title='test2',story_number=2,text='hogehogehoge\nfugafuga')


if __name__ == '__main__':
    test()