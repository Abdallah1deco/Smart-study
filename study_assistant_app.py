import streamlit as st
import tempfile
import os
import PyPDF2
import openai

# إعداد واجهة المستخدم
st.set_page_config(page_title="مساعد الدراسة الذكي", layout='wide')
st.title("📚 مساعد الدراسة الذكي")

# إعداد API KEY لـ OpenAI (يرجى استبدال 'YOUR_OPENAI_API_KEY' بمفتاحك)
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
openai.api_key = OPENAI_API_KEY

# دالة لتحليل نص PDF
def extract_pdf_text(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

# دالة البحث في النص
def search_in_text(full_text, query):
    query_lower = query.lower()
    found = []
    for idx, line in enumerate(full_text.split('\n')):
        if query_lower in line.lower():
            found.append((idx + 1, line))
    return found

# دالة توليد اختبار من كتاب باستخدام الذكاء الاصطناعي
def generate_quiz_from_text(text, n_questions=5):
    prompt = (
        f"أنت معلم محترف. الكتاب التالي عبارة عن مادة دراسية، "
        f"أنشئ اختبارًا مكونًا من {n_questions} أسئلة متعددة الخيارات بناءً على النص التالي، "
        f"واكتب الخيارات والإجابة الصحيحة بعد كل سؤال:\n\n{text[:1500]}\n\n"
        "اكتب الأسئلة بالعربية."
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "system", "content": prompt}], max_tokens=800
    )
    return response["choices"][0]["message"]["content"].strip()

# تحميل ملف PDF
uploaded_file = st.file_uploader("📄 قم بإرفاق ملف PDF للكتاب أو المادة", type=["pdf"])

if uploaded_file:
    # استخراج نص الكتاب
    with st.spinner("جارٍ استخراج النص من الملف..."):
        pdf_text = extract_pdf_text(uploaded_file)
    st.success("تم استخراج النص بنجاح!")

    # البحث في الكتاب
    st.subheader("🔍 البحث في الكتاب")
    search_query = st.text_input("اكتب كلمة أو جملة للبحث عنها في الكتاب")
    if search_query:
        results = search_in_text(pdf_text, search_query)
        if results:
            st.write(f"تم العثور على {len(results)} نتيجة:")
            for idx, line in results:
                st.markdown(f"**صفحة/سطر {idx}:** {line}")
        else:
            st.info("لم يتم العثور على نتائج.")

    # تحليل الكتاب وتوليد اختبار
    st.subheader("🤖 تحليل الكتاب وتوليد اختبار")
    num_questions = st.slider("عدد الأسئلة في الاختبار", 3, 10, 5)
    if st.button("توليد اختبار من محتوى الكتاب"):
        with st.spinner("يتم تحليل الكتاب وتوليد الاختبار..."):
            quiz = generate_quiz_from_text(pdf_text, n_questions=num_questions)
        st.markdown("### الاختبار المقترح:")
        st.write(quiz)
else:
    st.info("يرجى رفع ملف PDF للبدء.")

st.markdown("---")
st.caption("© 2025 مساعد الدراسة الذكي - جميع الحقوق محفوظة.")