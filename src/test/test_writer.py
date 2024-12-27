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
    print("title generation time: ", time.time() - start, "[s]")
    print(title)

    start = time.time()
    tags:list[str] = elyza.generate_tags()
    print("tag generation time: ", time.time() - start, "[s]")
    print(tags)
    
    # writer.save_test_story(title='test2',story_number=2,text='hogehogehoge\nfugafuga')


if __name__ == '__main__':
    test()