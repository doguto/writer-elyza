def enStr_tags(tags:list[str]) ->str:
    tagStr = ''
    for tag in tags:
        tagStr += '「' + tag + '」'
    return tagStr


TITLE_GENERATION = "なろう系の小説を作成しようとしています。「ゲーム転生」「モブ」というタグに合うようなネット小説の題名を1つ生成してください。なお、余計な返答や鍵括弧等は不要です。"


def generate_tag_prompt(title:str, tags:list[str]) ->str:
    tagStr = enStr_tags(tags)
    prompt = f"なろう系の小説を作成しようとしています。タイトルは{title}です。{tagStr}というタグに合うような、なろう系の単語を1つ生成してください。なお、余計な返答や鍵括弧、整理のための数字等は不要です。"
    return prompt


def generate_description_prompt(title:str, tags:list[str]) ->str:
    tagStr = enStr_tags(tags)
    prompt = f"なろう系の小説を作成しようとしています。タイトルは{title}です。{tagStr}というタグをこの小説には設定しています。これに合うようななろう系小説のあらすじを生成してください。読者が読みたくなるような文章で書いてください。例えば文末の句が同じものが続きすぎたり、句読点が多すぎたりすると読みづらいです。また、余計な返答や鍵括弧等は不要です。内容の矛盾にだけは注意！"
    return prompt


def generate_story_titles_prompt(title:str, tags:list[str], description:str, storyAmount:int=50) ->str:
    tagStr = enStr_tags(tags)
    prompt = f"なろう系の小説を作成しようとしています。タイトルは{title}です。{tagStr}というタグをこの小説には設定しています。また、あらすじは「{description}」です。全{str(storyAmount)}話で起承転結で物語を構成したいと考えています。一話につき5000字程を想定しているので、一話でストーリーがそこそこ進みます。第一話から第{storyAmount}話(最終話)までの話の題名を生成してください。余計な返答や鍵括弧等は不要です。内容の矛盾にだけは注意！ ちゃんとエンディングとか考えてね！"
    return prompt
