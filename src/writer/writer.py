import os
import sys
sys.path.append('../')
from writer.ai import Elyza, ChatGPT, AI
from novel.novel import Novel


class Writer():
    ai: AI
    novels: list[Novel]

    def __init__(self):
        self.ai = ChatGPT()
        self.novels = []
    

    def make_new_novel(self) ->Novel:
        title = self.ai.generate_title()
        newNovel = Novel(title)
        newNovel.basicInfo.add_tags(self.ai.generate_tags(title))
        newNovel.basicInfo.description = self.ai.generate_description(newNovel.basicInfo.title, newNovel.basicInfo.tags)
        self.novels.append(newNovel)
        return newNovel


    def make_plot(self, novel:Novel):
        storyTitles = self.ai.generate_story_titles(novel.basicInfo.title, novel.basicInfo.tags, novel.basicInfo.description)

    def save_story(self, title: str, story_number: int, text: str):
        title_dir = f'../../works/actual/{title}'
        if not os.path.isdir(title_dir):
            os.makedirs(title_dir, exist_ok=True)

        with open(f'{title_dir}/{story_number}.txt', mode='w') as f:
            f.write(text)

    def save_story(self, title: str, story_title: str, text: str):
        title_dir = f'../../works/actual/{title}'
        if not os.path.isdir(title_dir):
            os.makedirs(title_dir, exist_ok=True)

        with open(f'{title_dir}/{story_title}.txt', mode='w') as f:
            f.write(text)


    def save_test_story(self, title: str, story_number: int, text: str):
        title_dir = f'../../works/test/{title}'
        if not os.path.isdir(title_dir):
            os.makedirs(title_dir, exist_ok=True)

        with open(f'title_dir/{story_number}.txt', mode='w') as f:
            f.write(text)

    
