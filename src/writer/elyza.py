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
                    "content": "あなたは誠実で優秀な日本人のアシスタントです。特に指示が無い場合は、常に日本語で回答してください。",
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
    elyza.get_responce("カワウソについて、教えてください。")