from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("distilgpt2")

text = "I love AI"

result = tokenizer(text)

print(result)