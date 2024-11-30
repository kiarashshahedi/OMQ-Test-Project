# پروژه ارتباط کلاینت سرور با: ZeroMQ

ZeroMQ این پروژه یک برنامه کلاینت-سرور است که از 
برای ارتباطات استفاده می‌کند

## ویژگی‌ها
- پردازش دو نوع فرمان:
دستورات سیستم‌عامل و دستورات ریاضی (Math & OS)

- مدیریت چندین درخواست همزمان توسط سرور

- قابلیت توسعه‌پذیری برای افزودن انواع دستورات جدید

---
## نصب و اجرا

### پیش‌نیازها
1. نصب **Python 3.8+**
2. نصب وابستگی‌ها:
   ```bash
   pip install -r requirements.txt

## اجرا
1. سرور :
   ```bash
   python server.py
2. کلاینت :
   ```bash
   python client.py



## ساختار پروژه

project/
├── server/
    ├── command_handler.py  # مدیریت دستورات
    ├── logger.py     # مدیریت لاگ‌ها
    ├── server.py         # پیاده‌سازی سرور
    ├── tests/            # تست‌های واحد

├── client/
    ├── client.py         # پیاده‌سازی کلاینت
    ├── tests/            # تست‌های واحد


├── requirements.txt  # وابستگی‌ها
└── README.md         # مستندات


## تست‌ها
برای اجرای تست‌ها از دستور زیر استفاده کنید:
    '''bash
    pytest





