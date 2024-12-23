
class Story():
    chapter = 0
    title = ''
    text:str = ''
    isPublished = False

    def add_text(self, text:str):
        self.text += '\n'
        self.text += text

    def publish(self):
        self.isPublished = True



class BasicInfo():
    title:str
    description:str
    genre:int
    category:int
    length:int
    state:int
    regulation:int
    tags:list[str]
    isPublished:bool

    def __init__(self, title='', description='', genre=1, category=110400, length=3, state=2, regulation=0):
        self.title = title
        self.description = description

        # 0: no selection  # 1: for men  # 2: for wemen
        self.genre = genre
        
        # 110100: mistery   # 110200: horror     # 110300: SF       # 110400: fantasy
        # 110500: love      # 111400: character  # 111500: light    # 110600: blue-spring
        # 110700: current   # 110800: masses     # 111000: economy  # 111100: history
        # 111200: children  # 111300: picture    # 119000: BL       # 111600: essay
        self.category = category

        # 1: short-short  # 2: short  # 3: long
        self.length = length

        # 1: completed  # 2: writing now
        self.state = state

        # 0: no regulation  # 1: R-15  # 2: R-18
        self.regulation = regulation

        # can't set these parameters in constructer
        self.tags:list[str] = []
        self.isPublished = False


    def add_tags(self, tag:str):
        self.tags.append(tag)

    def publish(self):
        self.isPublished = True



class Novel():
    basicInfo:BasicInfo
    stories:list[Story]

    def add_story(self, story:Story):
        self.stories.append(story)

