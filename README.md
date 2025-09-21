```markdown
# 🧪 Client Automation Tests (Web + Mobile)

This project demonstrates **end-to-end client automation testing** for both **Web** (Selenium) and **Mobile** (Appium + Android Emulator).  

---

## 🚀 Features

### 🌐 Web Automation (Selenium + Pytest)
Automated tests against [the-internet.herokuapp.com](https://the-internet.herokuapp.com):
- ✅ **Login Flow** → handles valid & invalid login  
- ✅ **Form Validation** → validates email form submission  
- ✅ **File Upload** → uploads and verifies a file  

### 📱 Mobile Automation (Appium + Emulator)
Automated Android test cases:
- ✅ Launches and validates **Settings app** on emulator  
- ✅ Runs using **Appium v3** with **UiAutomator2 driver**  
- ✅ Captures emulator screenshots for evidence  

---

## 📂 Project Structure
```

client-automation-tests/
├── conftest.py # Shared fixtures (Selenium + Appium) + screenshots
├── tests/
│ ├── test_login.py # Web: login flow
│ ├── test_form_validation.py # Web: form validation
│ ├── test_file_upload.py # Web: file upload
│ └── test_mobile.py # Mobile: Settings app test
├── screenshots/ # Saved screenshots from test runs
├── requirements.txt # Python dependencies
├── pytest.ini # Pytest configuration
└── README.md

````

---

## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/hasanulkabir-md/Client-Testing-Automation.git
cd client-automation-tests
````

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Web Tests (Selenium)

Make sure Chrome/Chromedriver are installed:

```bash
pytest -v tests/test_login.py
pytest -v tests/test_form_validation.py
pytest -v tests/test_file_upload.py
```

### 5. Run Mobile Test (Appium + Emulator)

1. Start **Android Emulator** (AVD)
2. Start **Appium server** in another terminal:

   ```bash
   appium
   ```
3. Run the mobile test:

   ```bash
   pytest -v tests/test_mobile.py
   ```

---

## 📸 Screenshots

### ✅ Web Test (Login Success)

![Login Screenshot](screenshots/test_login_flow.png)

### ✅ Web Test (Form Validation)

![Form Validation Screenshot](screenshots/test_form_validation.png)

### ✅ Web Test (File Upload)

![File Upload Screenshot](screenshots/test_file_upload.png)

### ✅ Mobile Test (Appium + Emulator)

![Settings Screenshot](screenshots/settings_open.png)

---

## 📊 Tech Stack

* **Python 3.12**
* **Pytest** → test execution framework
* **Selenium** → web browser automation
* **Appium** → mobile automation
* **Android Emulator (AVD)** → for running APK/system app tests
* **Headless Chrome** → CI/CD-friendly web test execution

---

## 🎯 Why This Project?

This project highlights:

* Hands-on ability in **web + mobile automation**
* Experience with **QA process, debugging, and CI/CD-ready test frameworks**
* Clear **evidence of working tests** via screenshots

---

👨‍💻 **Author**: Md. Hasanul Kabir
🔗 [LinkedIn](https://linkedin.com/in/hasanulkabir_md) | [Portfolio](https://your-portfolio.com)

---


