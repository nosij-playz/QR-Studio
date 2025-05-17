
# 🎨 QR Code Studio

**QR Code Studio** is a sleek and modern desktop app to generate beautiful QR codes from any URL. Built with `Python`, `CustomTkinter`, and `qrcode`, it's the perfect tool for quick sharing and stylish presentation.

---

## 🚀 Features

- ✅ Beautiful GUI using `CustomTkinter`
- ✅ Paste any URL to generate QR code
- ✅ Save QR codes as `.png` images
- ✅ Clickable contact developer link
- ✅ Custom app icon
- ✅ Compiled `.exe` for Windows (no Python needed)

---

## 🖼️ Preview

![screenshot](screenshot.png) *(Include a screenshot of the app if you'd like)*

---

## 🧑‍💻 Developer Info

- 👨‍💻 Made with ❤️ by **NosijPlayz**
- 📬 [Contact the Developer](https://myporfolio-1o1h.onrender.com/contact)

---

## 📦 Requirements (for development)

If you're running the source code (`app.py`), install these dependencies:

```bash
pip install -r requirements.txt
```

### `requirements.txt`:

```
customtkinter
qrcode
pillow
```

---

## 🏗️ Build `.exe` (for developers)

To generate an `.exe` file using PyInstaller:

1. Install PyInstaller:

    ```bash
    pip install pyinstaller
    ```

2. Build the executable:

    ```bash
    pyinstaller --noconsole --onefile --icon=icon.ico app.py
    ```

3. Find your `.exe` in the `dist/` folder.

---

## 📁 Folder Structure

```
qr-code-studio/
├── app.py
├── icon.ico
├── requirements.txt
├── README.md
├── dist/
│   └── QRCodeStudio.exe
└── temp_qr.png (auto-generated)
```

---

## 📝 License

This project is open-source and free to use.

---

## 📬 Contact

For inquiries, feedback, or collaboration requests, please reach out via the contact form on my [portfolio website](https://myporfolio-1o1h.onrender.com/contact).
