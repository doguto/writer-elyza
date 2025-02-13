from typing import Union
from llama_cpp import Llama
from openai import OpenAI
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import writer.prompts as pr
import sys
sys.path.append('../../')
import environmental_variables as ev


class AI():
    llm: Union[Llama, OpenAI]
    
    def get_responce(self, input: str, maxTokens=1024, temperature=0.8) ->str:
        if type(self.llm) is Llama:
            response = self.llm.create_chat_completion(
                messages=[
                    {"role": "system", "content": "あなたは日本語のネット小説生成AIです。"},
                    {"role": "user", "content": input},
                ],
                seed=-1,
                max_tokens=maxTokens,  # 最大トークン数
                temperature=temperature,
            )
            return response["choices"][0]["message"]["content"]  
        elif type(self.llm) is OpenAI:
            response = self.llm.chat.completions.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": "あなたは日本語のネット小説生成AIです。"},
                    {"role": "user", "content": input},
                ],
                seed=-1,
                max_tokens=4092,  # 最大トークン数
                temperature=temperature,
            )
            return response.choices[0].message.content
        return ''


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


    

class Elyza(AI):
    def __init__(self):
        self.llm = Llama(
            model_path='../../elyza-models/Llama-3-ELYZA-JP-8B-q4_k_m.gguf',  # ダウンロードしたモデルのパス
            chat_format='llama-3',  # Llama 3のフォーマット指定
            n_ctx=8192,  # コンテキストの長さ  # limit of max_tokens
        )



class ChatGPT(AI):
    def __init__(self):
        self.llm = OpenAI(api_key=ev.OPENAI_API_KEY)



class DeepSeek(AI):
    def __init__(self):
        # トークナイザーとモデルの準備
        self.tokenizer = AutoTokenizer.from_pretrained(
            "deepseek-ai/DeepSeek-R1-Distill-Llama-8B"
        )

        self.llm = AutoModelForCausalLM.from_pretrained(
            "deepseek-ai/DeepSeek-R1-Distill-Llama-8B", 
            torch_dtype=torch.float16,
            device_map="auto"
        )
