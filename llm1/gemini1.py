from myllm.Myapi import geminiModel

model = geminiModel()

chat = model.start_chat(history=[])

print("\n--- Gemini 챗봇 시작 ---")

while True:

        user_message = input("나: ")

        if user_message.lower() == '종료':

                break

        response = chat.send_message(user_message)

        print("Gemini:", response.text)

print("--- 챗봇 종료 ---")
print(chat.history)
