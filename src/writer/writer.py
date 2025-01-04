import os
import sys
sys.path.append('../')
from writer.elyza import Elyza
from novel.novel import Novel


class Writer():
    elyza:Elyza
    novels:list[Novel]

    def __init__(self):
        self.elyza = Elyza()
        self.novels = []
    

    def make_new_novel(self) ->Novel:
        title = self.elyza.generate_title()
        newNovel = Novel(title=title)
        newNovel.basicInfo.add_tags(self.elyza.generate_tags(title=title))
        newNovel.basicInfo.description = self.elyza.generate_description(newNovel.basicInfo.title, newNovel.basicInfo.tags)
        self.novels.append(newNovel)
        return newNovel


    def make_plot(self, novel:Novel):
        storyTitles = self.elyza.generate_story_titles(novel.basicInfo.title, novel.basicInfo.tags, novel.basicInfo.description)

    def save_story(self, title:str, story_number:int, text:str):
        title_dir = '../../works/actual/' + title + '/'
        if not os.path.isdir(title_dir):
            os.makedirs(title_dir, exist_ok=True)

        with open(title_dir + str(story_number) + '.txt', mode='w') as f:
            f.write(text)

    def save_story(self, title:str, story_title:str, text:str):
        title_dir = '../../works/actual/' + title + '/'
        if not os.path.isdir(title_dir):
            os.makedirs(title_dir, exist_ok=True)

        with open(title_dir + story_title + '.txt', mode='w') as f:
            f.write(text)


    def save_test_story(self, title:str, story_number:int, text:str):
        title_dir = '../../works/test/' + title + '/'
        if not os.path.isdir(title_dir):
            os.makedirs(title_dir, exist_ok=True)

        with open(title_dir + str(story_number) + '.txt', mode='w') as f:
            f.write(text)

    
