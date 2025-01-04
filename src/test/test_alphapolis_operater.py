import sys
sys.path.append('../')
from web_operation_py.alphapolis_operater import AlphapolisOperaterPy
from src.novel.novel import Novel, Story, BasicInfo

def test():
    operater = AlphapolisOperaterPy()
    operater.sign_in()

    novel = Novel('hoge')
    novel.basicInfo.description = 'hogehoge\n','fugafuga\n','bahubahu'
    novel.basicInfo.tags.append('huggahuga')
    novel.basicInfo.tags.append('hoge')

    operater.make_new_novel(basicInfo=novel.basicInfo)

    operater.back_to_home()
    operater.move_to_edit_page(basicInfo=novel.basicInfo)

    story = Story('FUGAAA')
    story.add_text('hogehoge\nfugafuga\nhuhuhuhuhuhhhhhhhh')
    novel.add_story(story)
    operater.make_new_story(story, 'chapter', True)




if __name__ == '__main__':
    test()
    while True: 
        pass