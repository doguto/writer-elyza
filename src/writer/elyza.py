from llama_cpp import Llama
import writer.prompts as pr


class Elyza():
    def __init__(self):
        self.llm = Llama(
            model_path='../../elyza-models/Llama-3-ELYZA-JP-8B-q4_k_m.gguf',  # ダウンロードしたモデルのパス
            chat_format='llama-3',  # Llama 3のフォーマット指定
            n_ctx=8192,  # コンテキストの長さ  # limit of max_tokens
        )
    

    def get_responce(self, input: str, maxTokens=1024, temperature=0.8) ->str:
        response = self.llm.create_chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": "あなたは日本語のネット小説生成AIです。",
                },
                {
                    "role": "user",
                    "content": input,
                },
            ],
            seed=-1,
            max_tokens=maxTokens,  # 最大トークン数
            temperature=temperature,
        )
        return response["choices"][0]["message"]["content"]  


    def generate_title(self) ->str:
        responce = self.get_responce(input=pr.TITLE_GENERATION, maxTokens=512, temperature=0.90)
        title = self.adjust_generated_word(responce)
        return title
    
    def generate_tags(self, title: str) ->list[str]:
        tags: list[str] = ['ゲーム転生', 'モブ']
        for i in range(1, 7):
            prompt = pr.generate_tag_prompt(title=title, tags=tags)
            responce = self.get_responce(input=prompt, maxTokens=64, temperature=0.80)
            tag = self.adjust_generated_word(responce)
            tags.append(tag)
        return tags

    def generate_description(self, title: str, tags: list[str]) ->str:
        description = self.get_responce(pr.generate_description_prompt(title=title, tags=tags), temperature=0.72)
        return description


    def generate_story_titles(self, title: str, tags: list[str], description: str) ->list[str]:
        storyTitles = self.get_responce(pr.generate_story_titles_prompt(title, tags, description), maxTokens=4096, temperature=0.78)
        splitedTitles = storyTitles.splitlines()
        adjusetdTitles = []
        for title in splitedTitles:
            adjusetdTitles.append(title.strip('0123456789.一二三四五六七八九十話第「」 '))
        return adjusetdTitles
    

    # if you are trying to make first story, you have better to use description in last story.
    def generate_story(self, novel_title: str, story_title: str, story_number: int, last_story: str) ->str:
        story = self.get_responce(pr.get_story_generation_prompt(novel_title, story_title, story_number, last_story), maxTokens=8192, temperature=0.75)
        return story

    def adjust_generated_word(self, generatedWord: str) ->str:
        if generatedWord[0] != '「':
            return generatedWord
        # print('adjust ', generatedWord)        
        adjustedWord = generatedWord.strip('「」')
        return adjustedWord
