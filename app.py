import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk
import qrcode
import os
import webbrowser

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("🚀 QR Code Studio")
app.geometry("520x680")
app.resizable(False, False)

# ✅ Set custom window icon (Windows only)
try:
    app.iconbitmap("icon.ico")
except Exception as e:
    print(f"Warning: Could not load icon.ico – {e}")

# Fonts
font_title = ctk.CTkFont("Segoe UI", 28, weight="bold")
font_body = ctk.CTkFont("Segoe UI", 16)
font_status = ctk.CTkFont("Segoe UI", 14, slant="italic")

# Title
title = ctk.CTkLabel(app, text="🎨 QR Code Studio", font=font_title, text_color="#222")
title.pack(pady=(30, 10))

subtitle = ctk.CTkLabel(app, text="Create stylish QR codes from your URLs", font=font_body)
subtitle.pack(pady=(0, 20))

# URL input
url_entry = ctk.CTkEntry(app, placeholder_text="Paste your URL here...", width=420, height=40,
                         border_width=2, corner_radius=10)
url_entry.pack(pady=10)

# QR code display
qr_label = ctk.CTkLabel(app, text="")
qr_label.pack(pady=20)

# Status label
status_label = ctk.CTkLabel(app, text="", font=font_status, text_color="gray")
status_label.pack()

def generate_qr():
    url = url_entry.get().strip()
    if not url:
        status_label.configure(text="⚠️ Please enter a valid URL", text_color="red")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#000000", back_color="#ffffff")
    img.save("temp_qr.png")
    display_qr("temp_qr.png")
    status_label.configure(text="✅ QR Code Generated!", text_color="green")

def display_qr(path):
    img = Image.open(path).resize((260, 260))
    img = ImageTk.PhotoImage(img)
    qr_label.configure(image=img)
    qr_label.image = img

def save_qr():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")])
    if file_path:
        img = Image.open("temp_qr.png")
        img.save(file_path)
        status_label.configure(text="💾 Saved Successfully!", text_color="blue")

# Buttons
btn_frame = ctk.CTkFrame(app, fg_color="transparent")
btn_frame.pack(pady=15)

gen_btn = ctk.CTkButton(btn_frame, text="Generate QR", command=generate_qr, width=180, height=40,
                        hover_color="#29b6f6", corner_radius=15)
gen_btn.grid(row=0, column=0, padx=10)

save_btn = ctk.CTkButton(btn_frame, text="Save QR", command=save_qr, width=180, height=40,
                         hover_color="#66bb6a", corner_radius=15)
save_btn.grid(row=0, column=1, padx=10)

# Footer
footer = ctk.CTkLabel(app, text="Made with ❤️ by NosijPlayz", font=("Segoe UI", 12), text_color="gray")
footer.pack(side="bottom", pady=(10, 0))

# Clickable Contact Developer
def open_contact_page(event=None):
    webbrowser.open("https://myporfolio-1o1h.onrender.com/contact")

contact_link = ctk.CTkLabel(app, text="📬 Contact Developer", font=("Segoe UI", 12, "underline"),
                            text_color="#1e88e5", cursor="hand2")
contact_link.pack(side="bottom", pady=(0, 15))
contact_link.bind("<Button-1>", open_contact_page)

app.mainloop()
