
class Story():
    chapter = 0
    title = ''
    text:str = ''
    isPublished = False
    
    def set_chapter(self, chapter:int):
        self.chapter = chapter

    def set_title(self, title:str):
        self.title = title

    def set_text(self, text:str):
        self.text = text

    def add_text(self, text:str):
        self.text += '\n'
        self.text += text

    def publish(self):
        self.isPublished = True



class BasicInfo():
    def __init__(self, title='', description='', genre=1, category=110400, length=3, state=2, regulation=0):
        self.title = title
        self.description = description

        # 0: no selection  # 1: for men  # 2: for wemen
        self.genre:int = genre
        
        # 110100: mistery   # 110200: horror     # 110300: SF       # 110400: fantasy
        # 110500: love      # 111400: character  # 111500: light    # 110600: blue-spring
        # 110700: current   # 110800: masses     # 111000: economy  # 111100: history
        # 111200: children  # 111300: picture    # 119000: BL       # 111600: essay
        self.category:int = category

        # 1: short-short  # 2: short  # 3: long
        self.length = length

        # 1: completed  # 2: writing now
        self.state = state

        # 0: no regulation  # 1: R-15  # 2: R-18
        self.regulation = regulation

        # can't set these parameters in constructer
        self.tags:list[str] = []
        self.isPublished = False


    def set_title(self, title:str):
        self.title = title

    def set_description(self, description:str):
        self.description = description
    
    def set_genre(self, genre:int):
        self.genre = genre

    def set_category(self, category:int):
        self.category = category

    def set_length(self, length:int):
        self.length = length

    def set_state(self, state:int):
        self.state = state

    def set_regulation(self, regulation):
        self.regulation = regulation

    def add_tags(self, tag:str):
        self.tags.append(tag)

    def publish(self):
        self.isPublished = True



class Novel():
    basicInfo:BasicInfo
    stories:list[Story]


