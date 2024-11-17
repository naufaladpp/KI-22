from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    client_ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    log_ip(client_ip)
    return send_from_directory('', 'index.html')

def log_ip(ip_address):
    with open("ip_log.txt", "a") as file:
        file.write(f"Visitor IP: {ip_address}\n")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)