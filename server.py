from flask import Flask
from flask import request
app = Flask(__name__)
import time
import scrollphat

scrollphat.set_brightness(2)
scrollphat.set_rotate(True)

@app.route('/', methods=['POST'])
def parse_request():
    data = request.data
    scrollphat.write_string(data, " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

while True:
    try:
        scrollphat.scroll()
        time.sleep(0.1)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
