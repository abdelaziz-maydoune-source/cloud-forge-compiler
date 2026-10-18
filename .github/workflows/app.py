import streamlit as st
import requests
import json

st.set_page_config(page_title="منصة Cloud-Forge الذكية", layout="centered")
st.title("🏗️ منصة Cloud-Forge لتوليد تطبيقات الأندرويد")
st.subheader("صناعة هندسية مؤتمتة بالكامل بالذكاء الاصطناعي وبـ 0 درهم")

# المفاتيح السرية واسم الحساب المدمجة تلقائياً
GROQ_API_KEY = "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"
GITHUB_TOKEN = "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"
GITHUB_REPO = "abdelaziz-maydoune-source/cloud-forge-compiler"

user_idea = st.text_area("✍️ اكتب فكرة تطبيق الأندرويد الذي تريده بالتفصيل (مثال: تطبيق آلة حاسبة متطورة بلون أسود):")

if st.button("🚀 اطلق خط الإنتاج وصنع التطبيق الآن"):
    if user_idea:
        st.info("🧠 خطوة 1: يتم الآن تشفير الطلب وإرساله إلى الخوادم السحابية لـ Groq AI لمعالجة الفكرة البرمجية...")
        
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        prompt = f"You are an expert Android Developer. Generate a fully working Android App based on this idea: {user_idea}. Return ONLY the valid Java source code for MainActivity.java inside a markdown block, no explanations."
        
        data = {
            "model": "llama3-70b-8192",
            "messages": [{"role": "user", "content": prompt}]
        }
        
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
        
        if response.status_code == 200:
            ai_result = response.json()['choices']['message']['content']
            st.success("✅ خطوة 2: نجح الذكاء الاصطناعي في هندسة كود التطبيق وتوليد البنية التحتية بنجاح!")
            
            st.info("⚙️ خطوة 3: يتم الآن تفعيل خادم مايكروسوفت (GitHub Runner) وحقن الكود لبناء ملف الـ APK...")
            
            git_headers = {
                "Authorization": f"token {GITHUB_TOKEN}",
                "Accept": "application/vnd.github.v3+json"
            }
            
            git_data = {
                "event_type": "ai_code_trigger",
                "client_payload": {"code": ai_result}
            }
            
            git_response = requests.post(f"https://api.github.com/repos/{GITHUB_REPO}/dispatches", headers=git_headers, json=git_data)
            
            if git_response.status_code == 204:
                st.success("🎉 خطوة 4: تم تفعيل المصنع بنجاح! الخادم السحابي يبني التطبيق الآن.")
                st.markdown(f"🔗 [اضغط هنا لفتح لوحة تحكم المصنع السحابي ومتابعة الطبخ البرمجي وتحميل ملف الـ APK النهائي مجاناً](https://github.com/{GITHUB_REPO}/actions)")
            else:
                st.error("فشل في ربط البيانات مع خادم GitHub.")
        else:
            st.error("عذراً، فشل الاتصال بخادم الذكاء الاصطناعي المركّب.")
    else:
        st.warning("الرجاء كتابة فكرة التطبيق أولاً لتمريرها للمصنع.")
