#الكود انكتب بواسطه محمد الصياد SayyadN 
#التاريخ : 3-6-2025
#الكود مبني علي اداه SQLmap
#استعمله للغرض التعلم وهذا الكود يسهل علي المستخدم اسعمال اﻻداه ومدهومه بالذكاء اﻻصطناعي 
#الكود مفتوح المصدر ولكن لما تاخدخ وتعدل عليه اذكرني كمصدر وادعي دعوه ﻻمي

#استيراد المكتبات المطلوبة للعمل
import subprocess
import os
import google.generativeai as genai
import shutil
import time
import logging

#بعض المتغيرات للتسهيل
check = shutil.which
p = print
i = input
c_run = subprocess.run


# استبدل هذا بمفتاح API خاص بك في بيئة آمنة
API_KEY = "AIzaSyCDXhbDjtMMbKkm0FKGMr3SPAPaQ_aWYBQ"

def ai_help(error_message):
    try:
        # تهيئة المكتبة
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel("gemini-2.0-flash")

        while True:
            # إرسال الرسالة إلى نموذج الذكاء الاصطناعي
            response = model.generate_content(error_message)
            print("\n🔍 رد الذكاء الاصطناعي:")
            print(response.text)

            # سؤال المستخدم
            user_input = input("\nتقدر تخرج لما تكتب 'exit'. هل تريد المزيد من المساعدة؟ (Y/N): ").lower()

            if user_input in ["exit", "n"]:
                print("🚪 الخروج من المساعد الذكي.")
                break
            elif user_input == "y":
                error_message = input("🧠 أريد المعرفة عن المشكلة التي ظهرت: ")
            else:
                print("❌ خطأ في الإدخال، حاول مرة أخرى.")
    except Exception as ex:
        print("⚠️ الذكاء الاصطناعي غير متوفر حاليًا.")
        print(f"تفاصيل الخطأ: {ex}")

#السؤال في حال اﻻكمال او الخروج
def ask_continue(message="هل تريد حقا التكمله? (Y/N): "):
    try:
        while True:
            choice = input(message).strip().lower()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                print("جزاك الله خيرا -- جاري الخروج...")
                exit(0)
            else:
                print("ادخل خاطئ و جرب 'Y' or 'N'.")
    except Exception as e:
        ai_help(str(e))

#سلسه المهام القادمه سيكون عن تشغيل اوامر اﻻداه وتحليل المشكﻻت بالذكاء اﻻصطناعي

# استهداف URL معين
def target_url():
    try:
        target = i("من فضلك أدخل الرابط المستهدف :")
        cmd = ["sqlmap", "-u", target, "--batch"]
        c_run(cmd)
    except Exception as e:
        p("حدث خطأ أثناء اﻻستهداف")
        logging.error(e)
        p("جاري فتح مساعد الذكاء اﻻصطناعي")
        ai_help(str(e))
    ask_continue()

#الاتصال المباشر بقاعدة بيانات
def data_direct_conncet():
    try:
        data_url_direct = i("أدخل رابط اﻻتصال المباسر لقاعده البيانات :")
        cmd = ["sqlmap", "-d", data_url_direct, "--tables"]
        c_run(cmd)
    except Exception as e:
        p("حدث خطأ أثناء اﻻتصال")
        logging.error(e)
        p("جاري فتح مساعد الذكاء اﻻصطناعي")
        ai_help(str(e))
    ask_continue()

# تحليل سجل Log من Burp/WebScarab
def log_analyze():
    try:
        path = i("أدخل مسار الملف الخاص")
        cmd = ["sqlmap", "-l", path, "--batch"]
        c_run(cmd)
    except Exception as e:
        p("حدث خطأ أثناء العثور علي الملف")
        logging.error(e)
        p("جاري فتح مساعد الذكاء اﻻصطناعي")
        ai_help(str(e))
    ask_continue() 

#فحص عدة روابط من ملف
def scan_files_url():
    try:
        target_file = i("أدخل مسار الملف :")
        cmd = ["sqlmap", "-m", target_file, "--batch", "--dbs"]
        c_run(cmd)
    except Exception as e:
        p("حدث خطأ أثناء العثور علي الملف")
        logging.error(e)
        p("جاري فتح مساعد الذكاء اﻻصطناعي")
        ai_help(str(e))
    ask_continue() 

# تحميل طلب HTTP كامل من ملف
def http_request():
    try:
        target_file = i("أدخل مسار الملف :")
        cmd = ["sqlmap", "-r", target_file, "--batch", "--current-db"]
        c_run(cmd)
    except Exception as e:
        p("حدث خطأ أثناء العثور علي الملف")
        logging.error(e)
        p("جاري فتح مساعد الذكاء اﻻصطناعي")
        ai_help(str(e))
    ask_continue() 

#استخدام Google Dork كأداة بحث عن أهداف
def gdrok():
    try:
        target_url = i("أدخل الرابط المستهدف :") 
        cmd = ["sqlmap", "-g", target_url, "--batch"]
        c_run(cmd)
    except Exception as e:
        p("حدث خطأ أثناء العثور علي الرابط")
        logging.error(e)
        p("جاري فتح مساعد الذكاء اﻻصطناعي")
        ai_help(str(e))
    ask_continue() 

#تحميل إعدادات من ملف INI
def ini_setting():
    try:
        target_ini = ("أدخل مسار الملف المطلوب الخاص باﻻعدادات")
        cmd = ["sqlmap", "-c", target_ini ]
        c_run(cmd)
    except Exception as e:
        p("حدث خطأ أثناء العثور علي الرابط")
        logging.error(e)
        p("جاري فتح مساعد الذكاء اﻻصطناعي")
        ai_help(str(e))
    ask_continue() 

#تشغيل SQLmap بأسلوب مرشد تفاعلي
def tool_wizard():
    try:
        cmd = ["sqlmap", "--wizard"]
        c_run(cmd)
    except Exception as e:
        p("خطاء أثناء تشغيل المرشد التفاعلي")
        logging.error(e)
        p("جاري فتح مساعد الذكاء اﻻصطناعي")
        ai_help(str(e))
    ask_continue() 

#تحديث SQLmap من GitHub
def tool_base_update():
    try:
        cmd = ["sqlmap", "--update"]
        c_run(cmd)
    except Exception as e:
        p("خطأ أثناء تحديث اﻻداه")
        logging.error(e)
        p("جاري فتح مساعد الذكاء اﻻصطناعي")
        ai_help(str(e))
    ask_continue() 

#حذف كل بيانات التشغيل المخزنة
def delete():
    try:
        cmd = ["sqlmap", "--purge"]
        c_run(cmd)
    except Exception as e:
        p("خطأ أثناء حذف بيانات التشغيل")
        logging.error(e)
        p("جاري فتح مساعد الذكاء اﻻصطناعي")
        ai_help(str(e))
    ask_continue() 

#حذف مخرجات نتائج الفحوصات السابقة
def out_del():
    try:
        cmd = ["sqlmap", "--purge-output"]
        c_run(cmd)
    except Exception as e:
        p(" خطأ أثناء حذف بيانات مخرجات الفحوصات السابقة")
        logging.error(e)
        p("جاري فتح مساعد الذكاء اﻻصطناعي")
        ai_help(str(e))
    ask_continue() 

#التحقق من المتطلبات
def req_check():
    try:
        cmd = ["sqlmap", "--dependencies"]
        c_run(cmd)
    except Exception as e:
        p("خطأ أثناء التحقق من المتطلبات")
        logging.error(e)
        p("جاري فتح مساعد الذكاء اﻻصطناعي")
        ai_help(str(e))
    ask_continue() 

#طلب المساعده العاديه والمتقدمه
def help_n_a():
    try:
        cmd0 = ["sqlmap", "-h"]
        cmd1 = ["sqlmap", "-hh"]
        c_run(cmd0)
        c_run(cmd1)
    except Exception as e:
        p("خطأ أثناء طلب المساعده العاديه والمتقدمه معاً")
        logging.error(e)
        p("جاري فتح مساعد الذكاء اﻻصطناعي")
        ai_help(str(e))
    ask_continue() 

# عرض رقم إصدار SQLmap
def sqlmap_version():
    try:
        cmd = ["sqlmap", "--version"]
        c_run(cmd)
    except Exception as e:
        p("خطأ أثناء عرض رقم اﻻصدار الخاص باﻻداه")
        logging.error(e)
        p("جاري فتح مساعد الذكاء اﻻصطناعي")
        ai_help(str(e))
    ask_continue()

# تفعيل كل خصائص التحسين
def opt_options():
    try:
        target_url = i("أدخل الرابط المستهدف : ")
        cmd = ["sqlmap", "-u", target_url , "-o", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("خطأ أثناء تفعيل كل خصائص التحسين")
        logging.error(e)
        p("جاري فتح مساعد الذكاء اﻻصطناعي")
        ai_help(str(e))
    ask_continue()

# التنبؤ بمخرجات الاستعلامات
def pre_out():
    try:
        target_url = i("أدخل الرابط المستهدف : ")
        cmd = ["sqlmap", "-u", target_url, "--predict-output", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("خطأ أثناء التنبؤ بالمخرجات الخاصه باﻻستعلامات ")
        logging.error(e)
        p("جاري فتح مساعد الذكاء اﻻصطناعي")
        ai_help(str(e))
    ask_continue()

# استخدام اتصال HTTP دائم
def http_alive():
    try:
        target_url = i("أدخل الرابط المستهدف : ")
        cmd = ["sqlmap", "-u", target_url, "--keep-alive", "--batch"]
        c_run(cmd) 
    except Exception as e:
        p("خطأ أثناء ابقاء اﻻتصال دائم")
        logging.error(e)
        p("جاري فتح مساعد الذكاء اﻻصطناعي")
        ai_help(str(e))
    ask_continue()

#تجاهل محتوى الصفحة والتركيز على الطول
def ignore_html_content():
    try:
        target_url = i("أدخل الرابط المستهدف : ")
        cmd = ["sqlmap", "-u", target_url, "--null-connection", "--batch"]
        c_run(cmd) 
    except Exception as e:
        p("خطأ أثناء ابقاء اﻻتصال دائم")
        logging.error(e)
        p("جاري فتح مساعد الذكاء اﻻصطناعي")
        ai_help(str(e))
    ask_continue()

#عدد الاتصالات المتزامنة
def num_threads(threads_num=10):
    try:
        threads_num = i("أدخل عدد اﻻتصاﻻت المتزامنه اثناء الفحص (القيمه اﻻفتراضيه 10) : ")
        if user_input.strip():  # لو المستخدم كتب حاجة
            threads_num_user = int(threads_num)
        else:
            threads_num_user = 10  # لو ضغط Enter بدون إدخال
        target_url = i("أدخل الرابط المستهدف : ")
        cmd = ["sqlmap", "-u", target_url, f"--threads={threads_num}", "--batch"]
        c_run(cmd) 
    except Exception as e:
        p("خطأ أثناء تحديد اﻻتصالات المتزامنه")
        logging.error(e)
        p("جاري فتح مساعد الذكاء اﻻصطناعي")
        ai_help(str(e))
    ask_continue()

# اختصارات mnemonics
def use_mnemonics():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        mnemonics = i("أدخل mnemonics (مثال: bat,flu): ")
        cmd = ["sqlmap", "-u", target_url, "-z", mnemonics, "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء استخدام mnemonics.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# أمر نظام عند وجود SQLi
def alert_command():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        alert = i("أدخل أمر النظام للتنفيذ عند اكتشاف SQLi (مثال: notify-send 'SQLi Found'): ")
        cmd = ["sqlmap", "-u", target_url, f"--alert={alert}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء إعداد أمر التنبيه.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# صوت عند اكتشاف ثغرة
def beep_on_found():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--beep", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تشغيل التنبيه الصوتي.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تعطيل ألوان الإخراج
def disable_coloring():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--disable-coloring", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعطيل ألوان الإخراج.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# عرض سكربتات التمويه
def list_tampers():
    try:
        cmd = ["sqlmap", "--list-tampers"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء عرض السكربتات.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# العمل دون اتصال (وضع Offline)
def offline_mode():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--offline", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تفعيل الوضع دون اتصال.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# حفظ النتائج إلى ملف CSV
def results_to_file():
    try:
        targets_file = i("أدخل مسار ملف يحتوي على روابط مستهدفة (كل رابط في سطر): ")
        results_file = i("أدخل اسم ملف النتائج (مثال: results.csv): ")
        cmd = ["sqlmap", "-m", targets_file, f"--results-file={results_file}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء حفظ النتائج.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تشغيل واجهة Shell
def sqlmap_shell():
    try:
        cmd = ["sqlmap", "--shell"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تشغيل الواجهة التفاعلية.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تحديد مجلد مؤقت
def set_tmp_dir():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        tmp_dir = i("أدخل مسار المجلد المؤقت (مثال: ./tmp): ")
        cmd = ["sqlmap", "-u", target_url, f"--tmp-dir={tmp_dir}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعيين المجلد المؤقت.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تعديل الاتصال الغير مستقر
def unstable_mode():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--unstable", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تفعيل وضع الاتصال غير المستقر.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تحديد تقنيات SQLi المستخدمة
def choose_technique():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        techniques = i("أدخل الحروف الخاصة بالتقنيات (مثال: BEUSTQ): ")
        cmd = ["sqlmap", "-u", target_url, f"--technique={techniques}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء اختيار تقنيات SQLi.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تحديد تأخير الاستجابة في هجمات Blind Time-Based
def time_based_delay():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        delay = i("أدخل عدد الثواني لتأخير الاستجابة (القيمة الافتراضية 5): ")
        cmd = ["sqlmap", "-u", target_url, f"--time-sec={delay}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تحديد وقت التأخير.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تحديد عدد الأعمدة في فحص UNION
def union_columns_range():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        columns_range = i("أدخل مدى عدد الأعمدة (مثال: 1-10): ")
        cmd = ["sqlmap", "-u", target_url, f"--union-cols={columns_range}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تحديد عدد أعمدة UNION.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تحديد الحرف المستخدم في brute-force أعمدة UNION
def union_char():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        char = i("أدخل الحرف المستخدم في brute-force (مثال: A أو x): ")
        cmd = ["sqlmap", "-u", target_url, f"--union-char={char}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء إدخال حرف brute-force.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تحديد الجدول المستخدم في جملة FROM لهجوم UNION
def union_from_table():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        table = i("أدخل اسم الجدول المستخدم في FROM (مثال: users): ")
        cmd = ["sqlmap", "-u", target_url, f"--union-from={table}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تحديد جدول FROM.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# استخدام دومين خارجي لهجوم DNS exfiltration
def dns_exfiltration():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        domain = i("أدخل اسم النطاق المستخدم في exfiltration (مثال: yourdomain.com): ")
        cmd = ["sqlmap", "-u", target_url, f"--dns-domain={domain}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تهيئة هجوم DNS.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# رابط ثاني للنتيجة في هجوم second-order
def second_order_url():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        second_url = i("أدخل رابط النتيجة الثاني (Second-order): ")
        cmd = ["sqlmap", "-u", target_url, f"--second-url={second_url}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء إعداد second-order URL.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تحميل طلب HTTP ثاني من ملف للـ second-order
def second_order_request_file():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        req_file = i("أدخل مسار ملف الطلب الثاني (مثال: second.txt): ")
        cmd = ["sqlmap", "-u", target_url, f"--second-req={req_file}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تحميل طلب second-order.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# عمل fingerprint شامل
def full_fingerprint():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "-f", "--fingerprint", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء عمل بصمة للنظام.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# إضافة خيارات Request في دالة واحدة
def request_options():
    try:
        target_url = i("أدخل الرابط المستهدف (-u): ")
        user_agent = i("أدخل User-Agent (أو اتركه فارغًا): ")
        extra_header = i("أدخل هيدر إضافي (مثال: X-Forwarded-For: 127.0.0.1) (أو اتركه فارغًا): ")
        http_method = i("أدخل طريقة HTTP (POST, GET, PUT) (أو اتركه فارغًا): ").upper()
        post_data = i("أدخل بيانات POST (مثال: id=1) (أو اتركه فارغًا): ")
        param_delim = i("أدخل حرف تقسيم البراميتر (مثال: &) (أو اتركه فارغًا): ")

        cmd = ["sqlmap", "-u", target_url, "--batch"]

        if user_agent.strip():
            cmd += ["--user-agent", user_agent]

        if extra_header.strip():
            cmd += ["--headers", extra_header]

        if http_method.strip():
            cmd += ["--method", http_method]

        if post_data.strip():
            cmd += ["--data", post_data]

        if param_delim.strip():
            cmd += ["--param-del", param_delim]

        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء إعداد خيارات الطلب (Request).")
        logging.error(e)
        ai_help(str(e))
    ask_continue()


# مثال دالة أخرى بنفس النسق، مثلاً للـ fingerprint الكامل:
def full_fingerprint():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "-f", "--fingerprint", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء عمل بصمة للنظام.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# خيارات متقدمة للكوكيز، البروكسي، والهوست وغيرها في sqlmap
def advanced_request_options():
    try:
        target_url = i("أدخل الرابط المستهدف: ")

        cookie = i("أدخل قيمة الكوكي (مثال: PHPSESSID=a8d127e..) (أو اتركه فارغًا): ")
        cookie_del = i("أدخل حرف تقسيم الكوكيز (مثال: ;) (أو اتركه فارغًا): ")
        live_cookies = i("أدخل مسار ملف الكوكيز الحي (أو اتركه فارغًا): ")
        load_cookies = i("أدخل مسار ملف تحميل الكوكيز (أو اتركه فارغًا): ")
        drop_set_cookie = ask_yes_no("تجاهل Set-Cookie header؟")
        mobile = ask_yes_no("محاكاة موبايل User-Agent؟")
        random_agent = ask_yes_no("استخدام User-Agent عشوائي؟")
        host = i("أدخل قيمة Host header (أو اتركه فارغًا): ")
        referer = i("أدخل قيمة Referer header (أو اتركه فارغًا): ")
        auth_type = i("أدخل نوع التوثيق HTTP (Basic, Digest, NTLM, PKI) (أو اتركه فارغًا): ")
        auth_cred = i("أدخل بيانات التوثيق (name:password) (أو اتركه فارغًا): ")
        auth_file = i("أدخل مسار ملف الشهادة/المفتاح (أو اتركه فارغًا): ")
        ignore_code = i("أدخل كود خطأ HTTP لتجاهله (مثال: 401) (أو اتركه فارغًا): ")
        ignore_proxy = ask_yes_no("تجاهل إعدادات البروكسي الافتراضية للنظام؟")
        ignore_redirects = ask_yes_no("تجاهل عمليات إعادة التوجيه؟")
        ignore_timeouts = ask_yes_no("تجاهل انتهاء مهلة الاتصال؟")
        proxy = i("أدخل عنوان البروكسي (مثال: http://127.0.0.1:8080) (أو اتركه فارغًا): ")
        proxy_cred = i("أدخل بيانات توثيق البروكسي (name:password) (أو اتركه فارغًا): ")
        proxy_file = i("أدخل مسار ملف قائمة البروكسي (أو اتركه فارغًا): ")
        proxy_freq = i("أدخل عدد الطلبات بين تبديل البروكسي (أو اتركه فارغًا): ")

        cmd = ["sqlmap", "-u", target_url, "--batch"]

        if cookie.strip():
            cmd += ["--cookie", cookie]
        if cookie_del.strip():
            cmd += ["--cookie-del", cookie_del]
        if live_cookies.strip():
            cmd += ["--live-cookies", live_cookies]
        if load_cookies.strip():
            cmd += ["--load-cookies", load_cookies]
        if drop_set_cookie:
            cmd += ["--drop-set-cookie"]
        if mobile:
            cmd += ["--mobile"]
        if random_agent:
            cmd += ["--random-agent"]
        if host.strip():
            cmd += ["--host", host]
        if referer.strip():
            cmd += ["--referer", referer]
        if auth_type.strip():
            cmd += ["--auth-type", auth_type]
        if auth_cred.strip():
            cmd += ["--auth-cred", auth_cred]
        if auth_file.strip():
            cmd += ["--auth-file", auth_file]
        if ignore_code.strip():
            cmd += ["--ignore-code", ignore_code]
        if ignore_proxy:
            cmd += ["--ignore-proxy"]
        if ignore_redirects:
            cmd += ["--ignore-redirects"]
        if ignore_timeouts:
            cmd += ["--ignore-timeouts"]
        if proxy.strip():
            cmd += ["--proxy", proxy]
        if proxy_cred.strip():
            cmd += ["--proxy-cred", proxy_cred]
        if proxy_file.strip():
            cmd += ["--proxy-file", proxy_file]
        if proxy_freq.strip():
            cmd += ["--proxy-freq", proxy_freq]

        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء إعداد خيارات متقدمة للطلب.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# استخدام شبكة Tor لإخفاء الهوية
def use_tor():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--tor", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تفعيل استخدام شبكة Tor.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تحديد منفذ بروكسي Tor
def set_tor_port():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        tor_port = i("أدخل منفذ بروكسي Tor (الافتراضي 9050): ")
        if not tor_port.strip():
            tor_port = "9050"
        cmd = ["sqlmap", "-u", target_url, f"--tor-port={tor_port}", "--tor", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تحديد منفذ Tor.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تحديد نوع بروكسي Tor (HTTP, SOCKS4, SOCKS5)
def set_tor_type():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        tor_type = i("أدخل نوع بروكسي Tor (HTTP, SOCKS4, SOCKS5 - الافتراضي SOCKS5): ")
        if tor_type.strip().upper() not in ["HTTP", "SOCKS4", "SOCKS5"]:
            tor_type = "SOCKS5"
        cmd = ["sqlmap", "-u", target_url, f"--tor-type={tor_type.upper()}", "--tor", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تحديد نوع بروكسي Tor.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# التحقق من صحة استخدام Tor
def check_tor():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--check-tor", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء التحقق من Tor.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تأخير بين كل طلب HTTP بالثواني
def set_delay():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        delay = i("أدخل مدة التأخير بين كل طلب HTTP (بالثواني): ")
        if not delay.strip():
            delay = "0"
        cmd = ["sqlmap", "-u", target_url, f"--delay={delay}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء ضبط التأخير.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# ضبط مهلة الانتظار قبل انتهاء الاتصال
def set_timeout():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        timeout = i("أدخل مهلة الانتظار (بالثواني، الافتراضي 30): ")
        if not timeout.strip():
            timeout = "30"
        cmd = ["sqlmap", "-u", target_url, f"--timeout={timeout}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء ضبط مهلة الاتصال.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# ضبط عدد محاولات إعادة الاتصال بعد انتهاء المهلة
def set_retries():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        retries = i("أدخل عدد المحاولات بعد انتهاء المهلة (الافتراضي 3): ")
        if not retries.strip():
            retries = "3"
        cmd = ["sqlmap", "-u", target_url, f"--retries={retries}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء ضبط عدد المحاولات.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تغيير القيم لمعاملات معينة عشوائياً
def randomize_param():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        param = i("أدخل اسم المعامل/المعاملات لتغييرها عشوائياً (مثال: id,name): ")
        cmd = ["sqlmap", "-u", target_url, f"--randomize={param}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعيين التغيير العشوائي للمعاملات.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تحديد رابط آمن للزيارة المتكررة أثناء الاختبار
def safe_url():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        safe_url = i("أدخل عنوان URL آمن للزيارة المتكررة أثناء الاختبار: ")
        cmd = ["sqlmap", "-u", target_url, f"--safe-url={safe_url}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء ضبط الرابط الآمن.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# إرسال بيانات POST للرابط الآمن
def safe_post():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        safe_post = i("أدخل بيانات POST لإرسالها إلى الرابط الآمن: ")
        cmd = ["sqlmap", "-u", target_url, f"--safe-post={safe_post}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء ضبط بيانات POST للرابط الآمن.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تحميل طلب آمن من ملف
def safe_req():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        safe_req_file = i("أدخل مسار ملف الطلب الآمن: ")
        cmd = ["sqlmap", "-u", target_url, f"--safe-req={safe_req_file}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تحميل الطلب الآمن من ملف.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تحديد عدد الزيارات المنتظمة بين الزيارات للرابط الآمن
def safe_freq():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        freq = i("أدخل عدد الزيارات العادية بين كل زيارة للرابط الآمن: ")
        if not freq.strip():
            freq = "1"
        cmd = ["sqlmap", "-u", target_url, f"--safe-freq={freq}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء ضبط تكرار الزيارات للرابط الآمن.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تخطي ترميز URL للبيانات المرسلة
def skip_urlencode():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--skip-urlencode", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تخطي ترميز URL.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تعيين معامل CSRF token
def csrf_token():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        token = i("أدخل اسم معامل CSRF token: ")
        cmd = ["sqlmap", "-u", target_url, f"--csrf-token={token}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعيين CSRF token.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تعيين رابط استخراج CSRF token
def csrf_url():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        csrf_url = i("أدخل رابط استخراج CSRF token: ")
        cmd = ["sqlmap", "-u", target_url, f"--csrf-url={csrf_url}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعيين رابط CSRF.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تعيين طريقة استخراج CSRF token (GET, POST, ...)
def csrf_method():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        method = i("أدخل طريقة استخراج CSRF token (GET, POST, ...): ")
        cmd = ["sqlmap", "-u", target_url, f"--csrf-method={method}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعيين طريقة استخراج CSRF.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# عدد محاولات استخراج CSRF token
def csrf_retries():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        retries = i("أدخل عدد محاولات استخراج CSRF token (الافتراضي 0): ")
        if not retries.strip():
            retries = "0"
        cmd = ["sqlmap", "-u", target_url, f"--csrf-retries={retries}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعيين عدد محاولات CSRF.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# إجبار استخدام HTTPS/SSL
def force_ssl():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--force-ssl", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء فرض استخدام SSL.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# استخدام طلبات HTTP chunked مشفرة (POST)
def chunked():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--chunked", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تفعيل HTTP chunked.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# استخدام طريقة HTTP parameter pollution
def hpp():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--hpp", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تفعيل HTTP parameter pollution.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تنفيذ كود Python قبل الطلب
def eval_code():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        code = i("أدخل كود Python للتنفيذ قبل الطلب: ")
        cmd = ["sqlmap", "-u", target_url, f"--eval={code}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تنفيذ كود Python.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تحديد المعاملات التي سيتم اختبارها
def set_test_param():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        params = i("أدخل المعاملات التي تريد اختبارها (مثلاً: id,user): ")
        cmd = ["sqlmap", "-u", target_url, "-p", params, "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تحديد معاملات الاختبار.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تخطي اختبار معاملات معينة
def skip_params():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        skip_params = i("أدخل المعاملات التي تريد تخطي اختبارها (مثلاً: token,session): ")
        cmd = ["sqlmap", "-u", target_url, f"--skip={skip_params}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تخطي معاملات معينة.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تخطي اختبار المعاملات الثابتة (غير المتغيرة)
def skip_static_params():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--skip-static", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تخطي معاملات ثابتة.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# استبعاد معاملات حسب نمط معين (Regex)
def param_exclude():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        regex = i("أدخل تعبير Regex لاستبعاد معاملات معينة (مثلاً: ses): ")
        cmd = ["sqlmap", "-u", target_url, f"--param-exclude={regex}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء استبعاد معاملات بنمط معين.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# اختيار معاملات حسب مكانها (مثلاً: POST, GET)
def param_filter():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        place = i("أدخل مكان المعاملات المراد اختبارها (مثلاً: POST): ")
        cmd = ["sqlmap", "-u", target_url, f"--param-filter={place}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تصفية المعاملات حسب المكان.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# فرض نوع قاعدة البيانات (DBMS)
def force_dbms():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        dbms = i("أدخل نوع قاعدة البيانات (مثلاً: MySQL, PostgreSQL): ")
        cmd = ["sqlmap", "-u", target_url, f"--dbms={dbms}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء فرض نوع قاعدة البيانات.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# إضافة بيانات اعتماد لقاعدة البيانات
def dbms_credentials():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        creds = i("أدخل بيانات اعتماد قاعدة البيانات (user:password): ")
        cmd = ["sqlmap", "-u", target_url, f"--dbms-cred={creds}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء إضافة بيانات اعتماد قاعدة البيانات.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# فرض نظام تشغيل قاعدة البيانات
def force_os():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        os_name = i("أدخل نظام التشغيل المفروض لقاعدة البيانات (مثلاً: Windows, Linux): ")
        cmd = ["sqlmap", "-u", target_url, f"--os={os_name}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء فرض نظام تشغيل قاعدة البيانات.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# استخدام أرقام كبيرة كقيم لاغية للاختبار
def invalid_bignum():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--invalid-bignum", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تفعيل invalid-bignum.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# استخدام عمليات منطقية كقيم لاغية للاختبار
def invalid_logical():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--invalid-logical", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تفعيل invalid-logical.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# استخدام سلاسل عشوائية كقيم لاغية للاختبار
def invalid_string():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--invalid-string", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تفعيل invalid-string.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تعطيل ميكانيكية تحويل أنواع البيانات في الحمولة
def no_cast():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--no-cast", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعطيل تحويل أنواع البيانات.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تعطيل آلية الهروب للسلاسل النصية في الحمولة
def no_escape():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--no-escape", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعطيل الهروب للسلاسل النصية.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# إضافة بادئة للحمولة
def prefix_payload():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        prefix = i("أدخل بادئة للحمولة: ")
        cmd = ["sqlmap", "-u", target_url, f"--prefix={prefix}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء إضافة بادئة للحمولة.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# إضافة لاحقة للحمولة
def suffix_payload():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        suffix = i("أدخل لاحقة للحمولة: ")
        cmd = ["sqlmap", "-u", target_url, f"--suffix={suffix}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء إضافة لاحقة للحمولة.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# استخدام سكريبتات تلاعب مخصصة على بيانات الحمولة
def tamper_scripts():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        scripts = i("أدخل أسماء سكريبتات التلاعب (مفصولة بفواصل إذا أكثر من واحدة): ")
        cmd = ["sqlmap", "-u", target_url, f"--tamper={scripts}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء استخدام سكريبتات التلاعب.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تنفيذ أمر نظام تشغيل معين
def os_cmd():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        os_command = i("أدخل أمر نظام التشغيل للتنفيذ: ")
        cmd = ["sqlmap", "-u", target_url, f"--os-cmd={os_command}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تنفيذ أمر نظام التشغيل.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# فتح شل تفاعلي لنظام التشغيل
def os_shell():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--os-shell", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء فتح الشل التفاعلي لنظام التشغيل.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# فتح شل خارجي (OOB shell، Meterpreter أو VNC)
def os_pwn():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--os-pwn", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء فتح شل خارجي.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تنفيذ هجمة إعادة توجيه SMB (os-smbrelay)
def os_smbrelay():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--os-smbrelay", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تنفيذ هجمة SMB relay.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# استغلال ثغرة overflow في الذاكرة المؤقتة (buffer overflow) في الإجراءات المخزنة
def os_bof():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--os-bof", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء استغلال ثغرة buffer overflow.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# محاولة رفع صلاحيات مستخدم قاعدة البيانات
def priv_esc():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--priv-esc", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء محاولة رفع الصلاحيات.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تحديد مسار تثبيت إطار عمل Metasploit محليًا
def msf_path():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        path = i("أدخل المسار المحلي لإطار عمل Metasploit: ")
        cmd = ["sqlmap", "-u", target_url, f"--msf-path={path}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تحديد مسار Metasploit.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تحديد المسار المؤقت لملفات النظام عن بُعد
def tmp_path():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        path = i("أدخل المسار المؤقت للملفات على النظام الهدف: ")
        cmd = ["sqlmap", "-u", target_url, f"--tmp-path={path}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تحديد المسار المؤقت.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تحميل جلسة مخزنة من ملف sqlite
def load_session():
    try:
        session_file = i("أدخل مسار ملف الجلسة (.sqlite): ")
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "-s", session_file, "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تحميل الجلسة.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تسجيل حركة HTTP في ملف نصي
def log_http_traffic():
    try:
        traffic_file = i("أدخل اسم ملف تسجيل حركة HTTP: ")
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "-t", traffic_file, "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تسجيل حركة HTTP.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تعيين إجابات مسبقة
def set_answers():
    try:
        answers = i('أدخل الإجابات المُسبقة (مثال: "quit=N,follow=N"): ')
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, f"--answers={answers}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعيين الإجابات المسبقة.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تعيين براميترات تحتوي على بيانات Base64
def set_base64_params():
    try:
        params = i("أدخل البراميترات التي تحتوي على بيانات Base64 (مثال: 'param1,param2'): ")
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, f"--base64={params}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعيين براميترات Base64.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# استخدام أبجدية Base64 الآمنة URL واسم الملف
def use_base64_safe():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--base64-safe", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء استخدام أبجدية Base64 الآمنة.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تفعيل وضع batch (عدم طلب مدخلات المستخدم)
def batch_mode():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تفعيل وضع batch.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تعيين الحقول الثنائية (binary fields)
def set_binary_fields():
    try:
        fields = i("أدخل أسماء الحقول لتكون بنمط ثنائي (مثال: digest): ")
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, f"--binary-fields={fields}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعيين الحقول الثنائية.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# فحص اتصال الإنترنت قبل التقييم
def check_internet_connection():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--check-internet", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء فحص الاتصال بالإنترنت.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تنظيف قواعد بيانات sqlmap من UDF والجداول الخاصة
def cleanup_sqlmap():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--cleanup", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تنظيف sqlmap.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# الزحف على الموقع حتى عمق محدد
def crawl_site():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        depth = i("أدخل عمق الزحف (رقم): ")
        cmd = ["sqlmap", "-u", target_url, f"--crawl={depth}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء الزحف على الموقع.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# استثناء صفحات من الزحف
def crawl_exclude_pages():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        exclude = i("أدخل تعبير استثناء الصفحات من الزحف (مثال: logout): ")
        cmd = ["sqlmap", "-u", target_url, f"--crawl-exclude={exclude}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء استثناء صفحات من الزحف.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تعيين محدد CSV للفصل
def set_csv_delimiter():
    try:
        delimiter = i("أدخل محدد CSV (افتراضي ','): ")
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, f"--csv-del={delimiter}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعيين محدد CSV.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تعيين charset للاختبار العمياء Blind SQLi
def set_charset():
    try:
        charset = i("أدخل مجموعة الأحرف للاختبار العمياء (مثال: 0123456789abcdef): ")
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, f"--charset={charset}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعيين charset.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تحديد صيغة تصدير البيانات (CSV, HTML, SQLITE)
def set_dump_format():
    try:
        dump_format = i("أدخل صيغة تصدير البيانات (CSV, HTML, SQLITE): ").upper()
        if dump_format not in ["CSV", "HTML", "SQLITE"]:
            p("⚠️ صيغة غير مدعومة، سيتم استخدام CSV كافتراضي.")
            dump_format = "CSV"
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, f"--dump-format={dump_format}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعيين صيغة تصدير البيانات.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تعيين ترميز الأحرف (Encoding) لاسترجاع البيانات
def set_encoding():
    try:
        encoding = i("أدخل ترميز الأحرف (مثال: GBK): ")
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, f"--encoding={encoding}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعيين الترميز.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# عرض ETA (الوقت المقدر للوصول) لكل نتيجة
def show_eta():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--eta", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء عرض ETA.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تفريغ ملفات الجلسة للجهاز الحالي
def flush_session_files():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--flush-session", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تفريغ ملفات الجلسة.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# فحص وتحليل النماذج (Forms) في الصفحة
def parse_forms():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--forms", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تحليل النماذج.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تجاهل نتائج الاستعلامات المخزنة في الجلسة
def ignore_fresh_queries():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--fresh-queries", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تجاهل الاستعلامات المخزنة.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# استخدام نتائج Google dork بداية من صفحة معينة
def use_google_page():
    try:
        page = i("أدخل رقم صفحة Google dork للبدء منها: ")
        cmd = ["sqlmap", f"--gpage={page}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء استخدام صفحة Google dork.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تسجيل حركة HTTP في ملف HAR
def log_har_file():
    try:
        har_file = i("أدخل اسم ملف HAR لتسجيل حركة HTTP: ")
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, f"--har={har_file}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تسجيل ملف HAR.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# استخدام تحويل hex أثناء استرجاع البيانات
def use_hex():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--hex", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء استخدام تحويل hex.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تعيين مسار مخرج مخصص
def set_output_dir():
    try:
        output_dir = i("أدخل مسار مجلد المخرجات: ")
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, f"--output-dir={output_dir}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعيين مجلد المخرجات.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تحليل رسائل خطأ قاعدة البيانات من الردود
def parse_db_errors():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--parse-errors", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تحليل رسائل الخطأ.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# استخدام سكريبتات ما قبل المعالجة (preprocessing)
def preprocess_script():
    try:
        scripts = i("أدخل أسماء سكريبتات المعالجة المسبقة (مفصولة بفواصل): ")
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, f"--preprocess={scripts}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعيين سكريبتات المعالجة المسبقة.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# استخدام سكريبتات ما بعد المعالجة (postprocessing)
def postprocess_script():
    try:
        scripts = i("أدخل أسماء سكريبتات المعالجة اللاحقة (مفصولة بفواصل): ")
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, f"--postprocess={scripts}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعيين سكريبتات المعالجة اللاحقة.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# إعادة تفريغ (redump) الصفوف التي تحتوي على علامات غير معروفة
def repair_entries():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--repair", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء إعادة تفريغ الصفوف.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# حفظ الخيارات في ملف INI
def save_config():
    try:
        save_file = i("أدخل اسم ملف حفظ الإعدادات (INI): ")
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, f"--save={save_file}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء حفظ الإعدادات.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تعيين نطاق الهدف (Regexp)
def set_scope():
    try:
        scope = i("أدخل تعبير نطاق الهدف (Regexp): ")
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, f"--scope={scope}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعيين النطاق.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تخطي الكشف heuristics على ثغرات SQLi/XSS
def skip_heuristics():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--skip-heuristics", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تخطي الكشف heuristics.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تخطي الكشف heuristics على حماية WAF/IPS
def skip_waf():
    try:
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, "--skip-waf", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تخطي الكشف WAF.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تعيين بادئة للجداول المؤقتة
def set_table_prefix():
    try:
        prefix = i("أدخل بادئة للجداول المؤقتة (افتراضي sqlmap): ")
        if not prefix:
            prefix = "sqlmap"
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, f"--table-prefix={prefix}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعيين بادئة الجداول.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# اختيار اختبارات حسب payloads وعناوينها
def set_test_filter():
    try:
        test_filter = i('أدخل تصفية الاختبارات (مثال: "ROW"): ')
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, f"--test-filter={test_filter}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعيين تصفية الاختبارات.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تخطي اختبارات معينة حسب payloads وعناوينها
def set_test_skip():
    try:
        test_skip = i('أدخل اختبارات للتخطي (مثال: "BENCHMARK"): ')
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, f"--test-skip={test_skip}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعيين اختبارات للتخطي.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

# تعيين جذر ويب السيرفر
def set_web_root():
    try:
        webroot = i('أدخل جذر مستندات الويب للسيرفر (مثال: "/var/www"): ')
        target_url = i("أدخل الرابط المستهدف: ")
        cmd = ["sqlmap", "-u", target_url, f"--web-root={webroot}", "--batch"]
        c_run(cmd)
    except Exception as e:
        p("⚠️ خطأ أثناء تعيين جذر الويب.")
        logging.error(e)
        ai_help(str(e))
    ask_continue()

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def delay_print(text, delay=0.015):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

def main_menu():
    while True:
        clear()
        p("""
███    ██       ███████  ██████  ██                                              
████   ██       ██      ██    ██ ██                                              
██ ██  ██ █████ ███████ ██    ██ ██                                              
██  ██ ██            ██ ██ ▄▄ ██ ██                                              
██   ████       ███████  ██████  ███████                                         
                            ▀▀                                                   
                                                                                 
██████  ██    ██     ███████  █████  ██    ██ ██    ██  █████  ██████  ███    ██ 
██   ██  ██  ██      ██      ██   ██  ██  ██   ██  ██  ██   ██ ██   ██ ████   ██ 
██████    ████       ███████ ███████   ████     ████   ███████ ██   ██ ██ ██  ██ 
██   ██    ██             ██ ██   ██    ██       ██    ██   ██ ██   ██ ██  ██ ██ 
██████     ██        ███████ ██   ██    ██       ██    ██   ██ ██████  ██   ████ 
                                                                                 
                                                                                 
""")
        delay_print("\n🎯 استعمل هذه الاداة لغرض التعليم فقط", 0.01)
        delay_print("💡 تم تطويرها باستخدام الذكاء الاصطناعي لدعم الاستخدام الأخلاقي", 0.01)

        print("\n🔹 القائمة الرئيسية - اختر مهمة 🔹")

        functions = [
            ("استهداف رابط URL", target_url),
            ("الاتصال بقاعدة بيانات مباشرة", data_direct_conncet),
            ("تحليل ملف Log", log_analyze),
            ("فحص روابط متعددة من ملف", scan_files_url),
            ("تحميل طلب HTTP من ملف", http_request),
            ("فحص باستخدام Google Dork", gdrok),
            ("تحميل إعدادات من ملف INI", ini_setting),
            ("تشغيل الوضع الإرشادي (wizard)", tool_wizard),
            ("تحديث الأداة إلى أحدث إصدار", tool_base_update),
            ("حذف مجلد البيانات بالكامل", delete),
            ("حذف مجلد النتائج فقط", out_del),
            ("فحص المتطلبات والمكتبات", req_check),
            ("عرض المساعدة الكاملة", help_n_a),
            ("عرض إصدار sqlmap", sqlmap_version),
            ("تفعيل جميع التحسينات تلقائياً", opt_options),
            ("توقع نتائج الاستعلامات", pre_out),
            ("استخدام اتصالات HTTP مستمرة", http_alive),
            ("جلب طول الصفحة فقط بدون المحتوى", ignore_html_content),
            ("عدد الاتصالات المتزامنة", num_threads),
            ("تفعيل الرموز المختصرة في الإخراج", use_mnemonics),
            ("تشغيل أمر عند العثور على حقن", alert_command),
            ("تشغيل صوت عند العثور على ثغرة", beep_on_found),
            ("تعطيل تلوين المخرجات", disable_coloring),
            ("عرض سكربتات التلاعب المتاحة", list_tampers),
            ("العمل بدون اتصال بالإنترنت", offline_mode),
            ("حفظ النتائج إلى ملف CSV", results_to_file),
            ("فتح shell تفاعلي مع sqlmap", sqlmap_shell),
            ("تحديد مجلد مؤقت للملفات", set_tmp_dir),
            ("تفعيل الوضع غير المستقر", unstable_mode),
            ("اختيار تقنيات الحقن المستخدمة", choose_technique),
            ("ضبط تأخير الاستجابة الزمنية", time_based_delay),
            ("تحديد نطاق أعمدة UNION", union_columns_range),
            ("تحديد الحرف المستخدم في UNION", union_char),
            ("تحديد جدول في جملة FROM", union_from_table),
            ("هجوم استخراج البيانات عبر DNS", dns_exfiltration),
            ("الرابط المستخدم للاستجابة من النوع الثاني", second_order_url),
            ("تحميل طلب HTTP من النوع الثاني", second_order_request_file),
            ("عمل fingerprint شامل", full_fingerprint),
            ("إعدادات الطلب HTTP", request_options),
            ("إعدادات متقدمة للطلب", advanced_request_options),
            ("تفعيل Tor", use_tor),
            ("تحديد منفذ Tor", set_tor_port),
            ("تحديد نوع Tor Proxy", set_tor_type),
            ("التحقق من عمل Tor", check_tor),
            ("تحديد تأخير بين الطلبات", set_delay),
            ("ضبط مهلة الاتصال", set_timeout),
            ("ضبط عدد المحاولات", set_retries),
            ("تغيير عشوائي للمعاملات", randomize_param),
            ("رابط آمن لزيارته أثناء الفحص", safe_url),
            ("بيانات POST للرابط الآمن", safe_post),
            ("تحميل طلب آمن من ملف", safe_req),
            ("عدد الطلبات العادية بين الزيارات الآمنة", safe_freq),
            ("تخطي ترميز URL", skip_urlencode),
            ("تحديد اسم متغير CSRF", csrf_token),
            ("رابط صفحة استخراج CSRF", csrf_url),
            ("طريقة استخراج CSRF", csrf_method),
            ("عدد محاولات استخراج CSRF", csrf_retries),
            ("فرض استخدام HTTPS", force_ssl),
            ("تفعيل chunked encoding", chunked),
            ("تفعيل HPP", hpp),
            ("تشغيل كود Python مخصص", eval_code),
            ("تحديد المعاملات للاختبار", set_test_param),
            ("تخطي معاملات معينة", skip_params),
            ("تخطي المعاملات الثابتة", skip_static_params),
            ("استبعاد معاملات باستخدام regex", param_exclude),
            ("تصفية حسب مكان المعاملات", param_filter),
            ("فرض نوع قاعدة البيانات", force_dbms),
            ("تحديد بيانات اعتماد قاعدة البيانات", dbms_credentials),
            ("فرض نظام تشغيل القاعدة", force_os),
            ("قيم إلغاء وهمية كبيرة", invalid_bignum),
            ("قيم إلغاء باستخدام منطق", invalid_logical),
            ("قيم إلغاء نصية", invalid_string),
            ("تعطيل التحويلات", no_cast),
            ("تعطيل الهروب النصي", no_escape),
            ("إضافة بادئة للحمولة", prefix_payload),
            ("إضافة لاحقة للحمولة", suffix_payload),
            ("استخدام سكربتات tamper", tamper_scripts),
            ("تنفيذ أمر نظام", os_cmd),
            ("فتح shell نظام", os_shell),
            ("فتح جلسة Meterpreter/VNC", os_pwn),
            ("هجوم SMB relay", os_smbrelay),
            ("استغلال Buffer Overflow", os_bof),
            ("رفع صلاحيات المستخدم", priv_esc),
            ("تحديد مسار Metasploit", msf_path),
            ("تحديد مجلد مؤقت عن بُعد", tmp_path),
            ("تحميل جلسة محفوظة", load_session),
            ("تسجيل حركة HTTP في ملف", log_http_traffic),
            ("تعيين إجابات مسبقة", set_answers),
            ("تعيين براميترات Base64", set_base64_params),
            ("استخدام Base64 آمن", use_base64_safe),
            ("تفعيل وضع batch", batch_mode),
            ("الحقول الثنائية في النتائج", set_binary_fields),
            ("فحص اتصال الإنترنت", check_internet_connection),
            ("تنظيف قواعد بيانات sqlmap", cleanup_sqlmap),
            ("الزحف على الموقع", crawl_site),
            ("استثناء صفحات من الزحف", crawl_exclude_pages),
            ("تعيين فاصل CSV", set_csv_delimiter),
            ("تعيين charset لـ Blind SQLi", set_charset),
            ("تحديد صيغة استخراج البيانات", set_dump_format),
            ("تعيين ترميز الأحرف", set_encoding),
            ("عرض الوقت المتوقع للنتائج", show_eta),
            ("مسح ملفات الجلسة", flush_session_files),
            ("تحليل النماذج Forms", parse_forms),
            ("تجاهل استعلامات الجلسة السابقة", ignore_fresh_queries),
            ("Google Dork من صفحة محددة", use_google_page),
            ("تسجيل HAR", log_har_file),
            ("استخدام hex أثناء الاسترجاع", use_hex),
            ("تحديد مجلد الإخراج", set_output_dir),
            ("تحليل أخطاء DB", parse_db_errors),
            ("سكريبتات ما قبل المعالجة", preprocess_script),
            ("سكريبتات ما بعد المعالجة", postprocess_script),
            ("إعادة استخراج السجلات الغامضة", repair_entries),
            ("حفظ الإعدادات في ملف INI", save_config),
            ("تحديد نطاق الهدف", set_scope),
            ("تخطي الكشف heuristic", skip_heuristics),
            ("تخطي الكشف WAF", skip_waf),
            ("بادئة للجداول المؤقتة", set_table_prefix),
            ("تحديد اختبارات مخصصة", set_test_filter),
            ("تخطي اختبارات مخصصة", set_test_skip),
            ("جذر السيرفر Web Root", set_web_root),
        ]

        for idx, (label, _) in enumerate(functions, 1):
            print(f"[{idx}] {label}")
        print("[0] خروج")

        choice = i("\nأدخل رقم الخيار: ").strip()

        if choice == "0":
            p("\n👋 تم الخروج. دُمت في أمان الله.")
            break

        if choice.isdigit() and 1 <= int(choice) <= len(functions):
            _, func = functions[int(choice)-1]
            try:
                func()
            except Exception as e:
                p("⚠️ حدث خطأ في تنفيذ المهمة.")
                logging.error(e)
                ai_help(str(e))
        else:
            p("❌ خيار غير صحيح.")

        input("\n↩️ اضغط Enter للعودة للقائمة ...")
        

#لتشغيل الكود
main_menu()