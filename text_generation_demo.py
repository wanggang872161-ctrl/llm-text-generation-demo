from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

while True:
    prompt = input("请输入一句话（输入quit退出）：")

    if prompt == "quit":
        break

    result = generator(
        prompt,
        max_length=50
    )

    print("\n模型生成结果：")
    print(result[0]["generated_text"])
    print("-" * 50)
