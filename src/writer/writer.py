import os


class Writer():
    def __init__(self):
        pass

    def save_test_story(self, title:str, story_number:int, text:str):
        title_dir = '../../works/test/' + title + '/'
        if not os.path.isdir(title_dir):
            os.makedirs(title_dir, exist_ok=True)

        with open(title_dir + str(story_number) + '.txt', mode='w') as f:
            f.write(text)

    
    def save_story(self, title:str, story_number:int, text:str):
        title_dir = '../../works/actual/' + title + '/'
        if not os.path.isdir(title_dir):
            os.makedirs(title_dir, exist_ok=True)

        with open(title_dir + str(story_number) + '.txt', mode='w') as f:
            f.write(text)