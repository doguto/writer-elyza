from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


def initialize_elyza():
    tokenizer = AutoTokenizer.from_pretrained("elyza/ELYZA-japanese-Llama-2-7b-instruct")
    model = AutoModelForCausalLM.from_pretrained(
        "elyza/ELYZA-japanese-Llama-2-7b-instruct",
        torch_dtype=torch.float16,
        device_map="auto",
    )   


if __name__ == '__main__':
    initialize_elyza()