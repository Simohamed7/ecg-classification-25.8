from websocket import WebSocketApp
import threading

class WSClient:
    def __init__(self, url, on_message, on_error=None, on_close=None):
        self.url = url
        self.on_message = on_message
        self.on_error = on_error
        self.on_close = on_close
        self.ws = None
        self.thread = None

    def start(self):
        self.ws = WebSocketApp(self.url,
                               on_message=lambda ws, msg: self.on_message(msg),
                               on_error=lambda ws, e: self.on_error and self.on_error(e),
                               on_close=lambda ws, c, m: self.on_close and self.on_close(c, m))
        self.thread = threading.Thread(target=self.ws.run_forever, kwargs={"ping_interval":20, "ping_timeout":10}, daemon=True)
        self.thread.start()

    def stop(self):
        try:
            if self.ws:
                self.ws.close()
        except Exception:
            pass
