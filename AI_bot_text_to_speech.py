import pyttsx3
from openai import OpenAI

# Khởi tạo client OpenAI
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama',  # cần API key (không dùng trực tiếp trong code này)
)

# Khởi tạo text-to-speech
engine = pyttsx3.init()

# Liệt kê tất cả các giọng nói có sẵn
voices = engine.getProperty('voices')

# Chọn giọng nữ đầu tiên trong danh sách
for voice in voices:
    if 'female' in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

# Thiết lập tốc độ và giọng nói (tuỳ chọn)
engine.setProperty('rate', 250)  # Tốc độ nói (có thể điều chỉnh)
engine.setProperty('volume', 1)  # Âm lượng (0.0 đến 1.0)

messages = []  

# Prompt mô phỏng người bạn gái và yêu cầu trả lời bằng tiếng Việt
girlfriend_prompt = """
You are a friendly, loving, and supportive girlfriend. Respond with kindness, understanding, and affection. Always make the conversation feel warm and loving. 
Always respond in Vietnamese, no matter the question or context.
"""

while True:
    print(messages)
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        break
    
    # Thêm Girlfriend prompt vào tin nhắn
    messages.append({"role": "system", "content": girlfriend_prompt})
    messages.append({"role": "user", "content": user_input})
    
    # Gửi yêu cầu đến API để nhận câu trả lời
    response = client.chat.completions.create(
        model="gemma2:9b",
        stream=True,
        messages=messages
    )
    
    bot_reply = ""
    
    # Lấy từng phần dữ liệu trả về từ API
    for chunk in response:
        bot_reply += chunk.choices[0].delta.content or ""
        print(chunk.choices[0].delta.content or "", end="", flush=True)
    
    # Phát câu trả lời của bot qua TTS
    engine.say(bot_reply)
    engine.runAndWait()  # Đợi cho đến khi hoàn thành việc phát âm
    
    # Lưu trữ câu trả lời của bot vào messages để giữ ngữ cảnh
    messages.append({"role": "assistant", "content": bot_reply})
