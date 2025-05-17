# Smart-study
# منصة الدراسة الذكية

منصة متكاملة للدراسة تدعم:
- رفع وعرض ملفات PDF
- البحث داخل النصوص
- توليد اختبارات ذكية باستخدام الذكاء الاصطناعي
- تخزين الكتب والملفات الدراسية

## التقنيات المستخدمة
- Frontend: React.js
- Backend: Node.js/Express
- معالجة PDF: pdf-lib, react-pdf
- الذكاء الاصطناعي: OpenAI API

## كيفية التشغيل

### المتطلبات المسبقة
- Node.js (الإصدار 16 أو أحدث)
- npm أو yarn

### التنصيب
1. استنسخ المستودع:
```bash
git clone https://github.com/[اسم-المستخدم]/smart-study-platform.git
```

2. ثبت التبعيات:
```bash
cd smart-study-platform
npm install
cd frontend
npm install
```

3. تشغيل التطبيق:
```bash
# تشغيل الخادم
cd ..
node server.js

# تشغيل الواجهة الأمامية (في نافذة أخرى)
cd frontend
npm start
```

## المتغيرات البيئية المطلوبة
أنشئ ملف `.env` في المجلد الرئيسي وأضف:
```
OPENAI_API_KEY=your-api-key-here
PORT=5000
```
