class LogManager:
    def __init__(self, log_path='logs/logs.txt'):
        self.log_path = log_path

    def save_logs(self, text):
        with open(self.log_path, 'w') as file:
            file.write(text)
