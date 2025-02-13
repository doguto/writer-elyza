from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# トークナイザーとモデルの準備
tokenizer = AutoTokenizer.from_pretrained(
    "deepseek-ai/DeepSeek-R1-Distill-Llama-8B"
)

model = AutoModelForCausalLM.from_pretrained(
    "deepseek-ai/DeepSeek-R1-Distill-Llama-8B", 
    torch_dtype=torch.float16,
    device_map="auto"
)
