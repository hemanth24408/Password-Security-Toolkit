# 🔐 Password Security Toolkit

A modern password security application built with **Python** and **Streamlit** that helps users generate secure passwords, create memorable passphrases, and evaluate password strength using the **zxcvbn** password strength estimation algorithm.

This project was developed to explore password security concepts, improve Python programming skills, and build a practical application with a clean and interactive user interface.

---

# 📖 Overview

Weak passwords are one of the most common causes of security breaches. This application helps users generate strong passwords while also educating them about password security through real-time password strength analysis.

The toolkit provides multiple ways to create secure passwords and gives detailed feedback on their strength, estimated crack time, attack patterns, and security recommendations.

---

# ✨ Features

## 🔹 Instant Password Generator

* Generates highly random passwords instantly.
* Uses uppercase letters, lowercase letters, digits, and special characters.
* Ensures generated passwords meet a minimum strength threshold before displaying them.

**Screenshot**

<img width="2560" height="1246" alt="image" src="https://github.com/user-attachments/assets/75fc6d23-6daf-4e4e-bf3c-f64f544391ac" />



---

## 🔹 Custom Length Password Generator

Users can specify the desired password length.

Features include:

* Custom password length
* Random secure generation
* Password validation
* Strength filtering using zxcvbn

**Screenshot**

<img width="2556" height="1252" alt="image" src="https://github.com/user-attachments/assets/b2934368-3003-4040-8581-93067d80f3d3" />


---

## 🔹 Word-Based Passphrase Generator

Creates memorable passphrases by combining user-provided words with:

* Random uppercase/lowercase characters
* Random digits
* Special symbols

This provides passwords that are easier to remember while maintaining good security.

**Screenshot**

<img width="2560" height="1252" alt="image" src="https://github.com/user-attachments/assets/e6ae5432-a57b-4f8a-856b-eda21f0ce30f" />



---

## 🔹 Password Strength Meter

Evaluates any password entered by the user.

Displays:

* Password strength score
* Estimated number of guesses
* Detected password pattern
* Online attack crack time
* Offline attack crack time
* Security warnings
* Suggestions for improvement

**Screenshot**

<img width="2560" height="1246" alt="image" src="https://github.com/user-attachments/assets/8b004203-77f3-468c-ae6b-ddb56a1ebf19" />


---

# 🧠 Password Strength Analysis

The application uses **zxcvbn**, a widely used open-source password strength estimation library.

Instead of relying only on simple rules like:

* Minimum length
* One uppercase letter
* One special character

zxcvbn estimates password strength by analyzing:

* Dictionary words
* Common passwords
* Keyboard patterns
* Dates
* Repeated characters
* Sequential characters
* User behavior patterns
* Estimated cracking effort

This provides a much more realistic evaluation of password security.

---

# 🛠️ Technologies Used

* Python 3
* Streamlit
* CSS
* zxcvbn
* Random
* String

---

# 📂 Project Structure

```text
Password-Security-Toolkit/
│
├── assets/
│   └── background.webp
│
├── main.py
├── generator.py
├── strength.py
├── styles.css
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 💻 User Interface

The application is designed using Streamlit with custom CSS styling.

Interface highlights include:

* Modern layout
* Responsive sections
* Custom background
* Organized content
* Easy-to-use controls
* Interactive password analysis

---

# 🔒 Password Security Information

The application provides useful security information including:

* Password strength score
* Estimated number of guesses
* Password pattern identification
* Online attack estimation
* Offline attack estimation
* Security warnings
* Improvement suggestions

These insights help users understand why a password is strong or weak instead of only showing a simple rating.

---

# 📌 Future Improvements

Possible future enhancements include:

* Password history manager
* Password vault
* Breached password detection
* Password export options
* Password entropy visualization
* Dark/Light theme switch
* Multi-language support
* Password policy checker
* Copy success notification
* Password generation statistics

---

# 🙏 Acknowledgements

This project uses the **zxcvbn** password strength estimation algorithm.

* Original zxcvbn project by Dropbox:
  https://github.com/dropbox/zxcvbn

* Python implementation used in this project:
  https://github.com/dwolfhub/zxcvbn-python

Special thanks to the developers and contributors of the open-source community for making these resources available.

---

# 📄 Requirements

```
streamlit
zxcvbn
```

---

# 👨‍💻 Author

**D. Hemanth Reddy**

Python | Streamlit | Password Security | Open Source Learning

This project was developed as a personal learning project to strengthen Python development skills, explore password security concepts, and build a practical application suitable for a software development portfolio.

