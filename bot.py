# नीचे एक छोटा सा नकली वेब सर्वर जोड़ रहे हैं ताकि Render इसे फ्री वेब सर्विस मानकर बंद न करे
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive")

def run_health_server():
    # Render हमेशा 'PORT' नाम के एनवायरनमेंट वेरिएबल में पोर्ट देता है
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    server.serve_forever()

def main():
    # नकली वेब सर्वर को बैकग्राउंड में शुरू करें
    threading.Thread(target=run_health_server, daemon=True).start()

    app = Application.builder().token(TELEGRAM_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("aiquiz", start_ai_quiz))
    app.add_handler(CommandHandler("quiz", start_quiz_game))
    app.add_handler(MessageHandler(filters.FORWARDED & filters.POLL, handle_forwarded_poll))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_inputs))
    app.add_handler(CallbackQueryHandler(handle_callback_buttons))
    
    print("AI Quiz Bot aapke token ke sath shuru ho gaya hai...")
    app.run_polling()

if __name__ == '__main__':
    main()
