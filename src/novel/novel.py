class Novel():
    class BasicInfo():
        def __init__(self):
            self.title:str = ''
            self.description:str = ''

            # 0: no selection  # 1: for men  # 2: for wemen
            self.genre:int = 1
            
            # 110100: mistery   # 110200: horror     # 110300: SF       # 110400: fantasy
            # 110500: love      # 111400: character  # 111500: light    # 110600: blue-spring
            # 110700: current   # 110800: masses     # 111000: economy  # 111100: history
            # 111200: children  # 111300: picture    # 119000: BL       # 111600: essay
            self.category:int = 110400

            # 1: short-short  # 2: short  # 3: long
            self.length = 3

            # 1: completed  # 2: writing now
            self.state = 2

            # 0: no regulation  # 1: R-15  # 2: R-18
            self.regulation = 0

            self.tag:str = []


    class StoryInfo():
        def __init__(self):
            pass