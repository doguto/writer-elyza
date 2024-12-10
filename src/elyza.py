from transformers import AutoModelForCausalLM, AutoTokenizer

# モデル名
model_name = "elyza/ELYZA-japanese-Llama-2-7b-instruct"

# モデルとトークナイザーをロード
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)

print("Model and tokenizer loaded successfully!")
