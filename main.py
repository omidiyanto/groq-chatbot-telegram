import fitz  # PyMuPDF
from groq import Groq
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import asyncio
import csv
import os
from flask import Flask, render_template, send_file, request, redirect, url_for
from threading import Thread

# ubah variabel ini sesuai dengan API_KEY dan Token anda
GROQ_API_KEY="API_KEY_GROQ"
TOKEN_TELEGRAM_BOT="TOKEN_BOT_TELEGRAM"

# Inisialisasi Flask
app = Flask(__name__)

# Initialize global variables
pdf_path = "data.pdf"
pdf_text = ""
conversation_history = []
pdf_updated = False

# Fungsi untuk mengekstrak teks dari file PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_document = fitz.open(pdf_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

# Inisialisasi klien Groq
client = Groq(api_key=GROQ_API_KEY)

# Fungsi untuk memuat konten PDF
def load_pdf():
    global pdf_text, conversation_history
    pdf_text = extract_text_from_pdf(pdf_path)
    conversation_history = [{"role": "system", "content": "You are a chat assistant, only answer based on this data below:\n" + pdf_text}]

# Muat konten PDF awal
load_pdf()

# Fungsi untuk mencatat pertanyaan dan respons ke CSV
def log_to_csv(question, response):
    file_exists = os.path.isfile('log.csv')
    with open('log.csv', mode='a', newline='') as log_file:
        fieldnames = ['Pertanyaan', 'Response']
        writer = csv.DictWriter(log_file, fieldnames=fieldnames, delimiter=';')

        # Tulis header hanya jika file baru
        if not file_exists:
            writer.writeheader()
        
        writer.writerow({'Pertanyaan': question, 'Response': response})

# Fungsi untuk membaca log dari CSV
def read_log_from_csv():
    if not os.path.isfile('log.csv'):
        return []

    with open('log.csv', mode='r') as log_file:
        reader = csv.DictReader(log_file, delimiter=';')
        return list(reader)

# Route untuk halaman utama
@app.route('/')
def home():
    return render_template('index.html')

# Route untuk menampilkan log
@app.route('/logs')
def display_logs():
    logs = read_log_from_csv()
    return render_template('logs.html', logs=logs)

# Route untuk mereset log
@app.route('/reset', methods=['POST'])
def reset_logs():
    with open('log.csv', mode='w', newline='') as log_file:
        fieldnames = ['Pertanyaan', 'Response']
        writer = csv.DictWriter(log_file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()  # Write only the header
    return redirect(url_for('display_logs'))  # Redirect to logs page after reset


# Route untuk mendownload log CSV
@app.route('/download')
def download_log():
    return send_file('log.csv', as_attachment=True)

# Route untuk meng-upload file PDF
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    global pdf_updated
    success_message = None  # Initialize success message
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and file.filename.endswith('.pdf'):
            file.save(pdf_path)
            pdf_updated = True  # Set flag to indicate a new PDF has been uploaded
            load_pdf()  # Reload the PDF data immediately
            success_message = "File PDF berhasil di-upload!"  # Set success message
            return render_template('upload.html', success_message=success_message)  # Show message after upload

    return render_template('upload.html', success_message=success_message)  # Render page with potential message


# Fungsi untuk menangani pesan
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global pdf_updated
    if pdf_updated:
        load_pdf()  # Reload the PDF data if it was updated
        pdf_updated = False  # Reset the flag after reloading

    user_input = update.message.text
    conversation_history.append({"role": "user", "content": user_input})
    history_string = "\n".join(f"{msg['role']}: {msg['content']}" for msg in conversation_history)

    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": history_string}],
        model="llama3-8b-8192",
    )

    response = chat_completion.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": response})

    # Catat pertanyaan dan respons
    log_to_csv(user_input, response)

    await update.message.reply_text(response)

# Fungsi utama untuk memulai bot
async def main():
    app = ApplicationBuilder().token(TOKEN_TELEGRAM_BOT).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    await app.run_polling()

# Jalankan baik Flask maupun bot Telegram
if __name__ == '__main__':
    import nest_asyncio

    nest_asyncio.apply()
    
    # Jalankan aplikasi Flask dalam thread terpisah
    def run_flask():
        app.run(host="0.0.0.0", port=5000)

    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
