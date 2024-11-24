import json
import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


def update_b_label(event):
    # Получаем полное название базовой криптовалюты из словаря и обновляем метку
    code = base_combobox.get()
    name = currencies[code]
    b_label.config(text=name)

def exchange():
    """
    Получаем курс выбранной криптовалюты
    """
    code = base_combobox.get()
    name = currencies[code]

    if code:
        try:
            url = f'https://api.coingecko.com/api/v3/simple/price?ids={name}&vs_currencies=usd'
            headers = {
                "accept": "application/json",
                "x-cg-pro-api-key": "application/json"
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data_dict = json.loads(response.text)
            output_text = str(data_dict.get(name.lower()).get('usd', {})) + ' USD'
            b_label.config(text=output_text)
            mb.showinfo("Курс криптовалюты", f"Курс {output_text} за 1 {code}")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите криптовалюту")


# Словарь кодов криптовалют и их полных названий
currencies = {
    "BTC": "Bitcoin",
    "ETH": "Ethereum",
    "USDT": "Tether",
    "SOL": "Solana",
    "BNB": "BNB",
    "XRP": "XRP",
    "DOGE": "Dodecoin",
    "USDC": "USDC",
    "ADA": "Cardano",
    "STETH": "Lido Staked Ether",
    "TRX": "Tron"
}

# Создание графического интерфейса
win = Tk()
win.title("Курс популярных криптовалют")
w = win.winfo_screenwidth()
h = win.winfo_screenheight()
w2 = w // 2 - 250
h2 = h // 2 - 100
win.geometry(f"500x200+{w2}+{h2}")

Label(text="Базовая криптовалюта:").pack(padx=10, pady=5)
base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack(padx=10, pady=5)
base_combobox.bind("<<ComboboxSelected>>", update_b_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

Button(text="Получить курс выбранной криптовалюты", command=exchange).pack(padx=10, pady=10)

win.mainloop()
