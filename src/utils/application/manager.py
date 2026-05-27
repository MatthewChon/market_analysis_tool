import os
from dotenv import load_dotenv
from .pane import ApplicationPane
from alpaca.data import StockHistoricalDataClient

class ApplicationManager:
    def __init__(self) -> None:
        self.pane = ApplicationPane()
        self.stock_client = StockHistoricalDataClient(*self.get_credentials())

    def run(self) -> None:
        self.pane.root.mainloop()
    
    def get_credentials(self):
        load_dotenv()
        api_key = os.getenv("API_KEY")
        secret = os.getenv("SECRET")
        return api_key, secret

if __name__ == "__main__":
    manager = ApplicationManager()
    manager.run()