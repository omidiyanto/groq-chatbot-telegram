
## Generate GROQ API_KEY
Buka "https://console.groq.com/keys", Klik <b>Create API Key</b>
<img src="https://github.com/user-attachments/assets/40130610-80ad-41c8-b7cd-a909bf958fa0" >

Isi nama key nya bebas
<img src="https://github.com/user-attachments/assets/2647a4b5-3862-4cc9-8e33-eb2bec14d4e0">

Copy API_KEY yang anda dapatkan
<img src="https://github.com/user-attachments/assets/7f822bd0-d1ba-4eb7-bc78-e106b16f6c3d"> 

## Clone Github Project ini
Clone atau download project ini
```bash
git clone https://github.com/omidiyanto/groq-chatbot-example.git
```
Masuk dalam folder projectnya
```bash
cd groq-chatbot-example
```

## Isi API_KEY ke app.py
Copy paste API_KEY anda di <b>app.py</b>, bagian:
```
# Initialize conversation history and Groq client
conversation_history = []
client = Groq(
    api_key="API_KEY_GROQ_ANDA",
)
```
## Siapin contoh PDF sebagai data nya
Dalam chatbot ini akan membaca file "<b>data.pdf</b>" sebagai data referensi chatbotnya. 
Note: Siapkan data.pdf sebelum menjalankan chatbotnya !

 ## Jalanin Chatbot nya
 1) Install library yang dibutuhkan
	 ```bash
	 pip install -r requirements.txt
	 ```
 2) Run chatbotnya 
	 ```bash
	 python app.py
	 ```
