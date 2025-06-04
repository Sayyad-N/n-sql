# ملف التوثيق (README) - NSQL

## 🧠 نظرة عامة

**NSQL** هي أداة تفاعلية ذكية بُنيت على أساس SQLMap وسُخرت لتبسيط استخدامه للمبتدئين والمحترفين على حد سواء. تمت إضافة دعم الذكاء الاصطناعي للمساعدة في تحليل الأخطاء وتقديم حلول ذكية تلقائيًا.

**المطور:** محمد الصياد - "SayyadN"

> 🧕 *عند إعادة استخدام الكود أو تعديله، فضلاً اذكر المصدر وادعُ لأمي بالرحمة.*

---

## 🧩 مكونات المشروع:

- `nsql.py` : السكربت التفاعلي الرئيسي مبني على SQLMap
- `setup.sh` : سكربت التثبيت والإعداد التلقائي للبيئة

---

## ⚙️ طريقة التثبيت والتشغيل

```bash
chmod +x setup.sh
./setup.sh
python3 nsql.py
```

---

## 💡 الميزات

- دعم كامل لمعظم خيارات SQLMap مقسمة بوظائف سهلة.
- تشغيل مباشر للأوامر مثل: فحص روابط، اتصال مباشر، log analysis، google dork، إلخ.
- مساعد AI تلقائي عند حدوث خطأ.
- دعم Tor، وملفات Cookie، وخيارات حفظ النتائج.

---

## ⚠️ ملاحظات هامة

- يوجد مفتاح مدرج مسبقا Google API 
- يجب إدخال مفتاح Google API الخاص بك في المتغير `API_KEY` في `nsql.py` 
- السكربت مصمم لغرض التعليم والاختبار القانوني فقط
- يعمل على Linux و Windows

---

## 📜 الترخيص

مشروع مفتوح المصدر لأغراض التعليم فقط. أي استخدام غير قانوني يقع تحت مسؤوليتك الشخصية.

---

## ❤️ شكر خاص

لكل من يدعم تطوير أدوات عربية مفتوحة المصدر، ولكل من يذكر أم المبرمج بدعوة طيبة.

---

# README - NSQL (English)

## 🧠 Overview

**NSQL** is a smart interactive wrapper around SQLMap, developed to make it easier to use, especially for beginners. It includes built-in AI assistance via Google Gemini for automatic troubleshooting.

**Developer:** Mohammed El-Sayyad - "SayyadN"

> 🧕 Please mention the author and make a kind prayer for his mother if you reuse or modify the code.

---

## 🧩 Project Components:

- `nsql.py` : Main interactive Python wrapper for SQLMap
- `setup.sh` : Setup script to install requirements and update SQLMap

---

## ⚙️ Installation and Usage

```bash
chmod +x setup.sh
./setup.sh
python3 nsql.py
```

---

## 💡 Features

- Full SQLMap functionality organized into callable Python functions
- Easy execution of URL scans, direct DB connections, log analysis, Google dorks, etc.
- AI assistant for automatic error support
- Supports Tor, Cookie headers, INI settings, result export (CSV), and more

---

## ⚠️ Notes

- Insert your own Google API key in the `API_KEY` variable inside `nsql.py`
- This tool is for ethical, legal, and educational use only
- Compatible with Linux and Windows systems

---

## 📜 License

This is an open-source project for educational purposes. The author takes no responsibility for illegal use.

---

## ❤️ Special Thanks

To all who support Arabic open-source tools, and to everyone who sends a kind prayer for the developer's mother.
