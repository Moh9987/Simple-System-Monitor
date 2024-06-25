from flask import render_template
from app import app
import psutil

@app.route('/')
def index():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    return render_template('index.html', cpu_usage=cpu_usage, memory_info=memory_info)
