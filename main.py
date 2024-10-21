import fitz  # PyMuPDF
from groq import Groq
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import asyncio

# ubah variabel ini sesuai dengan API_KEY dan Token anda
GROQ_API_KEY="API_KEY_GROQ"
TOKEN_TELEGRAM_BOT="TOKEN_BOT_TELEGRAM"

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_document = fitz.open(pdf_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# Load PDF content
pdf_path = "data.pdf"
pdf_text = extract_text_from_pdf(pdf_path)

# Initialize conversation history
conversation_history = [{"role": "system", "content": "You are a chat assistant, only answer based on this data below:\n" + pdf_text}]

# Function to handle messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_input = update.message.text
    conversation_history.append({"role": "user", "content": user_input})
    history_string = "\n".join(f"{msg['role']}: {msg['content']}" for msg in conversation_history)

    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": history_string}],
        model="llama3-8b-8192",
    )

    response = chat_completion.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": response})
    await update.message.reply_text(response)

# Main function to start the bot
async def main():
    app = ApplicationBuilder().token(TOKEN_TELEGRAM_BOT).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    await app.run_polling()

if __name__ == '__main__':
    import nest_asyncio
    nest_asyncio.apply()
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
