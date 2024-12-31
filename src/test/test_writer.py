import time
import sys
sys.path.append('../')
from writer.writer import Writer
from writer.elyza import Elyza

def test():
    writer = Writer()
    elyza = Elyza()
    
    titleGenerationStart = time.time()
    title = elyza.generate_title()
    titleGenerationTime = time.time()

    tagsGenerationStart = time.time()
    tags:list[str] = elyza.generate_tags(title=title)

    
    print("title generation time: ", titleGenerationTime - titleGenerationStart, "[s]")
    print(title)
    print("tag generation time: ", time.time() - tagsGenerationStart, "[s]")
    print(tags)
    
    # writer.save_test_story(title='test2',story_number=2,text='hogehogehoge\nfugafuga')


if __name__ == '__main__':
    test()