import time
import sys
sys.path.append('../')
from writer.writer import Writer
from writer.ai import Elyza, ChatGPT

def test():
    writer = Writer()
    ai = ChatGPT()
    
    titleGenerationStart = time.time()
    title = ai.generate_title()
    titleGenerationTime = time.time()
    print('succeeded in title generation.\n')

    tagsGenerationStart = time.time()
    tags:list[str] = ai.generate_tags(title=title)
    tagsGenerationTime = time.time()
    print('succeeded in tags generations.\n')

    descriptionGenerationStart = time.time()
    description:str = ai.generate_description(title=title, tags=tags)
    descriptionGenerationTime = time.time()
    print('succeeded in description generation.\n')

    plotStart = time.time()
    plot = ai.generate_story_titles(title, tags, description)
    plotFin = time.time()
    print('succeeded in titles generations.\n')

    story_start = time.time()
    story = ai.generate_story(title, plot[0], 1, description)
    story_fin = time.time()
    print('succeeded in story generation.\n')

    
    print("title generation time: ", titleGenerationTime - titleGenerationStart, "[s]")
    print(title)
    print("tag generation time: ", tagsGenerationTime - tagsGenerationStart, "[s]")
    print(tags)
    print('description generation time: ', descriptionGenerationTime - descriptionGenerationStart, '[s]')
    print(description)
    print('plot generation time: ', plotFin - plotStart)
    print(plot)
    print('story generation time is: ', story_fin - story_start, '[s]')
    print(story)
    
    # writer.save_test_story(title='test2',story_number=2,text='hogehogehoge\nfugafuga')


def test_title_list_generation():
    elyza = Elyza()
    writer = Writer()

    plotStart = time.time()
    plot = elyza.generate_story_titles(
        '最弱のプレイヤーが最底辺のモブに転生してしまった', 
        ['ゲーム転生', 'モブ', '異世界', '無双', '最強の魔導士', '最凶', '最弱のプレイヤーが最底辺のモブに転生してしまった', '過酷'], 
        '最弱のプレイヤーが最底辺のモブに転生してしまった。何もかもが最低の世界に、男は足を踏み入れた。'
        +'「最強の魔導士」が支配する世界。最凶のモンスターが闊歩し、人々はひたすらに生き延びる日々を送る。そんな中、男は最弱のプレイヤーとしてゲー ムに身を捧げたが、最底辺のモブに転生してしまった。'
        +'元の世界では無双と謳われていた男は、異世界ではただの弱者。過酷な環境に耐えかね、男は死に体でいた。だが、死の間際に一つの光が見えた。最強 の魔導士の目に留まり、男は新たな命を与えられた。'
        +'最弱のプレイヤーが最底辺のモブに転生してしまった。新たな世界で男は何を為すのか。'
    )
    plotFin = time.time()
    print('succeeded in titles generations.\n')
    print('plot generation time: ', plotFin - plotStart)
    print(plot) 


if __name__ == '__main__':
    test()
    # test_title_list_generation()