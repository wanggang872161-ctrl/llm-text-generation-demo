from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis"
)

while True:
    text = input("请输入一句英文（输入quit退出）：")

    if text == "quit":
        break

    result = classifier(text)

    print("\n分析结果：")
    print(result)
    print("-" * 50)