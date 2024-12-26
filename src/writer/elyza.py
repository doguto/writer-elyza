from llama_cpp import Llama
import writer.prompts as pr


class Elyza():
    def __init__(self):
        self.llm = Llama(
            model_path="../../elyza-models/Llama-3-ELYZA-JP-8B-q4_k_m.gguf",  # ダウンロードしたモデルのパス
            chat_format="llama-3",  # Llama 3のフォーマット指定
            n_ctx=1024,  # コンテキストの長さ
        )
    

    def get_responce(self, input:str) ->str:
        print(input)
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
            max_tokens=1024,  # 最大トークン数
        )
        return response["choices"][0]["message"]["content"]  


    def generate_title(self) ->str:
        title = self.get_responce(pr.TITLE_GENERATION)
        return title
    
    def generate_tags(self) ->list[str]:
        tags:list[str] = []
        for i in range(10):
            tag = self.get_responce()
            tags.append(tag)

    def generate_description(self, title:str) ->str:
        description = self.get_responce()
        return description



if __name__ == '__main__':
    elyza = Elyza()
    responce = elyza.get_responce("以下の要素を持つネット小説のプロットを25話分作成してください。「ゲーム転生、なろう系、男主人公=モブ、剣と魔法」") # Test
    print(responce)