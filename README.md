## TRY THE DEMO
https://dashboard-chatbot.omidiyanto.my.id/ <br><br>
http://t.me/ominewchatbot

## Buat Bot Telegram
1. Cari dan buka <b>botfather</b> di telegram lalu klik "START"
<img src="https://github.com/user-attachments/assets/a357e8ae-33a9-4037-abc2-1a94d8707f5b"></img>
2. Buat bot baru dengan pesan <b>/newbot</b> ikut panduannya untuk memasukkan nama bot di telegramnya, nantinya akan ada <b>TOKEN</b> yang diberikan, catat token ini karena akan digunakan nanti
<img src="https://github.com/user-attachments/assets/47666538-61af-444c-ad60-d223cdf0cf36"></img>
3. Chatbot di telegram bisa diakses pada link yang diberikan, contohnya seperti ini
<img src="https://github.com/user-attachments/assets/4a482215-d17e-487a-b2ce-38e4ef34578c"></img>


## Generate GROQ API_KEY
Buka "https://console.groq.com/keys", Klik <b>Create API Key</b>
<img src="https://github.com/user-attachments/assets/40130610-80ad-41c8-b7cd-a909bf958fa0" ></img>

Isi nama key nya bebas
<img src="https://github.com/user-attachments/assets/2647a4b5-3862-4cc9-8e33-eb2bec14d4e0"></img>

Copy API_KEY yang anda dapatkan
<img src="https://github.com/user-attachments/assets/7f822bd0-d1ba-4eb7-bc78-e106b16f6c3d"> </img>

## Clone Github Project ini
Clone atau download project ini
```bash
git clone https://github.com/omidiyanto/groq-chatbot-telegram.git
```
Masuk dalam folder projectnya
```bash
cd groq-chatbot-telegram
```

## Isi API_KEY dan Token telegram ke app.py
Copy paste API_KEY dan token bot telegram anda di <b>app.py</b>, bagian:
```
# ubah variabel ini sesuai dengan API_KEY dan Token anda
GROQ_API_KEY="API_KEY_GROQ"
TOKEN_TELEGRAM_BOT="TOKEN_BOT_TELEGRAM"
```
## Siapin contoh PDF sebagai data nya
Dalam chatbot ini akan membaca file "<b>data.pdf</b>" sebagai data referensi chatbotnya. <br>
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
3) Coba chat melalui telegram bot yang telah dibuat
<img src="https://github.com/user-attachments/assets/7bad6ea0-733e-4d6b-a4c3-b8be763bc489"></img>
<br>
Selamat, Chatbot anda telah berhasil diimplementasikan dan siap menjawab pertanyaan anda sesuai data PDF yang anda berikan !!
<br>

4) Buka Dashboard Management di browser dengan URL http://localhost:5000
<img src="https://github.com/user-attachments/assets/d8d57f58-1454-4b76-aba4-72cddd067c64"></img>
