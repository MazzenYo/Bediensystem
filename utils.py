import time
from datetime import datetime


def format_time(timestamp=time.time()):
    return datetime.fromtimestamp(timestamp).strftime("%H:%M:%S:%f")
