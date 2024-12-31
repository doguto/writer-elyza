TITLE_GENERATION = "なろう系の小説を作成しようとしています。「ゲーム転生」「モブ」というタグに合うようなネット小説の題名を1つ生成してください。なお、余計な返答や鍵括弧等は不要です。"


def generate_tag_prompt(title:str, tags:list[str]):
    tagStr:str = ''
    for tag in tags:
        tagStr += '「' + tag + '」' 
    prompt = f"なろう系の小説を作成しようとしています。タイトルは{title}です。{tagStr}というタグに合うような、なろう系の単語を1つ生成してください。なお、余計な返答や鍵括弧等は不要です。"
    return prompt
