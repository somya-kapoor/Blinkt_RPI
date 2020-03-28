from flask import *
from blinkt import set_pixel, set_brightness, show, clear
import colorsys
import time

app = Flask(__name__)

@app.route("/")
def home():	
    return render_template('index.html')

@app.route('/off')
def off():
    clear()
    show()
    return render_template('index.html')

@app.route('/mwl')
def mwl():    
    t = 2
    while t > 0:
        for i in range(8):
            clear()
            set_pixel(i, 255, 255, 255)
            show()
            time.sleep(0.05)
        t = t - 1  
    return render_template('index.html')  
        
@app.route('/rainbow')
def rainbow():     
    spacing = 360.0 / 16.0
    hue = 0
    set_brightness(0.1)
    t = 16
    while t > 0:
        hue = int(time.time() * 100) % 360
        for x in range(8):
            offset = x * spacing
            h = ((hue + offset) % 360) / 360.0
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
            set_pixel(x, r, g, b)
        show()
        time.sleep(0.05)
        t = t - 1
            
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
