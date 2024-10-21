import fitz  # PyMuPDF
from groq import Groq

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_document = fitz.open(pdf_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

# Initialize conversation history and Groq client
conversation_history = []
client = Groq(
    api_key="API_KEY_GROQ_ANDA",
)

# Add system prompt at the beginning
conversation_history.append({"role": "system", "content": "You are a chat assistant, only answer based on this data below:\n"})

# Ask for PDF file path
pdf_path = "data.pdf"
pdf_text = extract_text_from_pdf(pdf_path)
conversation_history.append({"role": "system", "content": pdf_text})  # Add PDF content to history

print("PDF content loaded. You can now start asking questions about it.")

while True:
    user_input = input("Masukkan Pertanyaan (atau 'quit' untuk keluar): ")
    
    if user_input.lower() == 'quit':
        break

    # Update conversation history
    conversation_history.append({"role": "user", "content": user_input})
    history_string = "\n".join(f"{msg['role']}: {msg['content']}" for msg in conversation_history)

    # Generate completion from Groq
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": history_string},
        ],
        model="llama3-8b-8192",
    )
    
    response = chat_completion.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": response})

    print(response)
    print()
