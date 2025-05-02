# Selenium Python Automation - Web Interaction Examples

This project demonstrates how to automate browser interactions using **Selenium with Python**, including navigating web pages, simulating searches, clicking links, and filling out login forms.

---

## 📜 Requirements

Make sure you have the following installed:

- Python 3.x
- Google Chrome
- ChromeDriver (compatible with your Chrome version)
- Selenium library

---

🔹 Note:
If you want to use send_keys(Keys.ENTER), it works as if you are typing text and pressing Enter at the same time. This is useful for search bars or forms that automatically submit when Enter is pressed.

Example:
```
from selenium.webdriver.common.keys import Keys
element.send_keys("example text", Keys.ENTER)
```
🔸 But if you just want to click on a button or a link, use:
```
element.click()
```

### ✅ Install Selenium

```bash
pip install selenium
