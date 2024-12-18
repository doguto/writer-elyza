import sys
sys.path.append('../')
from web_operation_py.alphapolis_operater import AlphapolisOperaterPy
from src.novel.novel import Novel

def test():
    operater = AlphapolisOperaterPy()
    operater.sign_in()

    novel = Novel()
    info = novel.BasicInfo()
    info.title = 'hoge'
    info.description = 'hogehoge\n','fugafuga\n','bahubahu'
    info.tags.append('huggahuga')
    info.tags.append('hoge')

    operater.make_new_works(novelBasicInfo=info)

    operater.back_to_home()
    operater.move_to_edit_page(novelBasicInfo=info)


if __name__ == '__main__':
    test()
    while True: 
        pass