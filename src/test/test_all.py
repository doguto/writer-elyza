import sys
sys.path.append('../')
from web_operation_py.alphapolis_operater import AlphapolisOperaterPy
from writer.writer import Writer
from novel.novel import Novel, BasicInfo, Story


def main() ->None:
    writer = Writer()
    operater = AlphapolisOperaterPy()

    operater.sign_in()
    newNovel = writer.make_new_novel()
    operater.make_new_novel(newNovel.basicInfo)

    


if __name__ == '__main__': 
    main()
    while True: 
        pass