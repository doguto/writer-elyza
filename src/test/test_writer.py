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
    tagsGenerationTime = time.time()

    descriptionGenerationStart = time.time()
    description:str = elyza.generate_description(title=title, tags=tags)
    descriptionGenerationTime = time.time()

    plotStart = time.time()
    plot = elyza.generate_story_titles(title, tags, description)
    plotFin = time.time()

    
    print("title generation time: ", titleGenerationTime - titleGenerationStart, "[s]")
    print(title)
    print("tag generation time: ", tagsGenerationTime - tagsGenerationStart, "[s]")
    print(tags)
    print('description generation time: ', descriptionGenerationTime - descriptionGenerationStart, '[s]')
    print(description)
    print('plot generation time: ', plotFin - plotStart)
    print(plot)
    
    # writer.save_test_story(title='test2',story_number=2,text='hogehogehoge\nfugafuga')


if __name__ == '__main__':
    test()