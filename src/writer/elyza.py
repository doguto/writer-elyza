from llama_cpp import Llama


class Elyza():
    def __init__(self):
        self.llm = Llama(
            model_path="../../elyza-models/Llama-3-ELYZA-JP-8B-q4_k_m.gguf",  # ダウンロードしたモデルのパス
            chat_format="llama-3",  # Llama 3のフォーマット指定
            n_ctx=1024,  # コンテキストの長さ
        )
    

    def get_responce(self, input:str):
        response = self.llm.create_chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": "あなたは日本人のネット小説家です。条件に適するネット小説を作成してください。",
                },
                {
                    "role": "user",
                    "content": input,
                },
            ],
            max_tokens=1024,  # 最大トークン数
        )
        
        # 結果の出力
        print(response["choices"][0]["message"]["content"])



if __name__ == '__main__':
    elyza = Elyza()
    elyza.get_responce("以下の要素を持つネット小説のプロットを25話分作成してください。「ゲーム転生、なろう系、男主人公=モブ、剣と魔法」") # Test