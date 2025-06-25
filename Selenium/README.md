# Selenium Python Automation - Web Interaction Examples

This project demonstrates how to automate browser interactions using **Selenium with Python**, including navigating web pages, simulating searches, clicking links, and filling out login forms.

🔹 Note:
* Run all these scripts in Jupyter Notebook, because the browser will only close when the Jupyter session ends. Otherwise, it will remain open even after the script finishes running.

* However, when you run the same script in an IDE, the browser closes automatically as soon as the script completes.


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

### ✅ 1: Install Selenium

```bash
pip install selenium
```
### ✅ 2: Install WebDriver Manager

```bash
pip3 install webdriver-manager
```

| Method         | Priority | Example                                     |
| -------------- | -------- | ------------------------------------------- |
| `ID`           | ✅✅✅      | `driver.find_element(By.ID, "myid")`        |
| `Name`         | ✅✅       | `driver.find_element(By.NAME, "myname")`    |
| Relative XPath | ✅✅       | `//input[@value='Customer Menu']`           |
| CSS Selector   | ✅        | `input.button-input[value='Customer Menu']` |
| Absolute XPath | ❌        | `/html/body/div[1]/form/input[2]`           |

