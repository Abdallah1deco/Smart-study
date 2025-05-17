const express = require('express');
const multer = require('multer');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
const upload = multer({ dest: 'uploads/' });

// Middleware
app.use(cors());
app.use(express.json());

// تخزين الملفات المؤقت
if (!fs.existsSync('uploads')) {
  fs.mkdirSync('uploads');
}

// API لرفع الملفات
app.post('/api/upload', upload.single('pdf'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('لم يتم رفع أي ملف');
  }

  const fileInfo = {
    filename: req.file.originalname,
    path: req.file.path,
    size: req.file.size,
    uploadedAt: new Date()
  };

  res.json({
    message: 'تم رفع الملف بنجاح',
    file: fileInfo
  });
});

// API للبحث في النصوص
app.post('/api/search', (req, res) => {
  const { text, query } = req.body;
  
  if (!text || !query) {
    return res.status(400).send('النص أو كلمة البحث مطلوبة');
  }

  const results = {
    matches: text.split(query).length - 1,
    excerpts: text.includes(query) ? [
      text.substring(text.indexOf(query) - 20, text.indexOf(query) + 20)
    ] : []
  };

  res.json(results);
});

// API لتوليد الأسئلة
app.post('/api/generate-test', (req, res) => {
  const { text } = req.body;
  
  if (!text) {
    return res.status(400).send('النص مطلوب لتوليد الأسئلة');
  }

  // محاكاة استجابة الذكاء الاصطناعي
  const mockResponse = {
    questions: [
      {
        question: "ما هو الموضوع الرئيسي للنص؟",
        options: ["العلوم", "التاريخ", "الأدب", "الفن"],
        answer: 0
      },
      {
        question: "ما هي الفكرة الأساسية في الفقرة الأولى؟",
        options: ["تقديم الموضوع", "عرض الأمثلة", "شرح النظرية", "كل ما سبق"],
        answer: 3
      }
    ]
  };

  res.json(mockResponse);
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`الخادم يعمل على المنفذ ${PORT}`);
});