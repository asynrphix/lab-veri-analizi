from dotenv import load_dotenv
import os
import pandas as pd
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

df = pd.read_csv("analiz_sonucu.csv")
asan_gunler = df[df["Limit_Asimi"] == True]

metin = "Limiti aşan günler:\n"
for _, satir in asan_gunler.iterrows():
    metin += f"- {satir['gun']}: % Silica Concentrate = {satir['% Silica Concentrate']}\n"

prompt = f"""Aşağıda bir maden/laboratuvar sürecinde, normal seviyenin üzerinde ölçülen silika (istenmeyen madde) oranlarının listesi var. 
Ortalama seviye 2.32, hesaplanan limit 3.41.

{metin}

Bu verilere dayanarak, bir laboratuvar/kalite kontrol raporuna eklenecek 3-4 cümlelik kısa, profesyonel bir Türkçe yorum yaz. 
Genel gözlemi belirt (örneğin hangi aylarda yoğunlaştığı), olası bir öneri ekle. Teknik ama anlaşılır bir dil kullan."""

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)

yorum = response.text
yorum = yorum.replace("**", "")
print("AI Yorumu:")
print(yorum)

with open("ai_yorumu.txt", "w", encoding="utf-8") as f:
    f.write(yorum)

print()
print("Kaydedildi: ai_yorumu.txt")