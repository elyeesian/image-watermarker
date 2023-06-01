from PIL import ImageTk, Image
import tkinter as tk
from tkinter import filedialog


uploaded = False
filename = ''
watermark = None
final_img = None

def save_img():
    final_img.save(fp='/Users/goddang/Downloads/watermarked.png')

def UploadWM():
    global watermark
    fp = filedialog.askopenfilename()
    watermark = Image.open(fp)
    watermark = watermark.resize((50, 50))
    watermark.putalpha(64)
    if watermark:
        label = tk.Label(text='Watermark uploaded')
        label.pack()


def UploadAction():
    print(watermark.size)
    global filename
    global final_img
    global uploaded
    filename = filedialog.askopenfilename()
    uploaded = True
    print(filename)
    im = watermark
    img = ImageTk.PhotoImage(image=Image.open(filename))
    w = img.width()
    h = img.height()
    img.paste(im, box=((w/2) - 10, (h/2) - 10))
    canvas = tk.Canvas(width=w, height=h)
    canvas.create_image(w/2, h/2, image=img)
    canvas.pack()
    final_img = Image.open(img)
    if final_img:
        save_btn = tk.Button(text="Save Image", command=save_img)
        save_btn.pack()


window = tk.Tk()
window.title("Image Watermarking App")
window.minsize(500, 500)
window.config(padx=50, pady=50)

print(f"filename: {filename}")
button = tk.Button(text='Upload Watermark', command=UploadWM)
button.pack()
upload_button = tk.Button(text='Upload Image', command=UploadAction)
upload_button.pack()

print("over.")



window.mainloop()