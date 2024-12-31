from llama_cpp import Llama
import writer.prompts as pr


class Elyza():
    def __init__(self):
        self.llm = Llama(
            model_path="../../elyza-models/Llama-3-ELYZA-JP-8B-q4_k_m.gguf",  # ダウンロードしたモデルのパス
            chat_format="llama-3",  # Llama 3のフォーマット指定
            n_ctx=4096,  # コンテキストの長さ  # limit of max_tokens
        )
    

    def get_responce(self, input:str, maxTokens:int=1024, temperature=0.8) ->str:
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
    
    def generate_tags(self, title:str) ->list[str]:
        tags:list[str] = ["ゲーム転生", "モブ"]
        for i in range(1, 7):
            prompt = pr.generate_tag_prompt(title=title, tags=tags)
            responce = self.get_responce(input=prompt, maxTokens=64, temperature=0.80)
            tag = self.adjust_generated_word(responce)
            tags.append(tag)
        return tags

    def generate_description(self, title:str) ->str:
        description = self.get_responce()
        return description

    def adjust_generated_word(self, generatedWord:str) ->str:
        if generatedWord[0] != '「':
            return generatedWord
        # print('adjust ', generatedWord)        
        adjustedWord = generatedWord.strip('「」')
        return adjustedWord
