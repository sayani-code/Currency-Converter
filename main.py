import tkinter as tk
from tkinter import ttk, messagebox
import threading
 
from converter import convert
from utils import is_valid_amount, is_valid_currency_name, format_result,format_result


CURRENCY_NAMES = {
    "USD": "US Dollar",
    "EUR": "Euro",
    "GBP": "Pound Sterling",
    "JPY": "Japanese Yen",
    "INR": "Indian Rupee",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Yuan",
    "SGD": "Singapore Dollar",
    "NZD": "New Zealand Dollar",
    "ZAR": "South African Rand",
    "AED": "UAE Dirham",
    "SEK": "Swedish Krona",
    "MXN": "Mexican Peso",
    "BRL": "Brazilian Real",
}


BANNER_COLOR = "#305271"      # deep teal
BANNER_TEXT_COLOR = "#ffffff"
ACCENT_COLOR = "#326840"
BACKGROUND_COLOR = "#dbddc9"
ANSWER_BG = "#f2f5f7"
LINK_COLOR = "#2C265A"

def dropdown_values():
    """Build the 'CODE - Name' strings shown in each dropdown."""
    return [f"{code} - {name}" for code, name in CURRENCY_NAMES.items()]
 
def code_from_dropdown(value):
    """Pull just the 3-letter code out of a 'CODE - Name' string."""
    return value.split(" - ")[0].strip().upper()
 

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("420x460+50+50")
        self.root.resizable(False, False)
        self.root.configure(bg=BACKGROUND_COLOR)
 
        self._build_widgets()
 
    # ------------------------------------------------------------------
    # UI construction
    # ------------------------------------------------------------------
    def _build_widgets(self):
        self._build_banner()
        self._build_currency_key_link()
        self._build_amount_input()
        self._build_currency_dropdowns()
        self._build_buttons()
        self._build_answer_panel()
 
    def _build_banner(self):
        banner = tk.Frame(self.root, bg=BANNER_COLOR, height=54)
        banner.pack(fill="x")
        banner.pack_propagate(False)
        tk.Label(
            banner,
            text="Currency Converter",
            bg=BANNER_COLOR,
            fg=BANNER_TEXT_COLOR,
            font=("Helvetica", 16, "bold"),
        ).pack(expand=True)
 
    def _build_currency_key_link(self):
        link = tk.Label(
            self.root,
            text="Currency Key",
            bg=BACKGROUND_COLOR,
            fg=LINK_COLOR,
            font=("Helvetica", 10, "underline"),
            cursor="hand2",
        )
        link.pack(pady=(12, 6))
        link.bind("<Button-1>", lambda event: self.show_currency_key())
 
    def _build_amount_input(self):
        tk.Label(
            self.root,
            text="Value to Convert:",
            bg=BACKGROUND_COLOR,
            font=("Helvetica", 11, "bold"),
        ).pack(pady=(4, 2))
 
        self.amount_entry = tk.Entry(
            self.root,
            font=("Helvetica", 12),
            justify="center",
            highlightthickness=2,
            highlightbackground="#cccccc",
            highlightcolor=ACCENT_COLOR,
            relief="flat",
        )
        self.amount_entry.insert(0, "100")
        self.amount_entry.pack(padx=40, fill="x", ipady=4)
 
    def _build_currency_dropdowns(self):
        values = dropdown_values()
 
        row_from = tk.Frame(self.root, bg=BACKGROUND_COLOR)
        row_from.pack(fill="x", padx=30, pady=(16, 6))
        tk.Label(
            row_from, text="From:", width=6, anchor="w",
            bg=BACKGROUND_COLOR, font=("Helvetica", 11, "bold"),
        ).pack(side="left")
        self.from_box = ttk.Combobox(row_from, values=values, state="readonly")
        self.from_box.set(values[0])  # USD - US Dollar
        self.from_box.pack(side="left", fill="x", expand=True)
 
        row_to = tk.Frame(self.root, bg=BACKGROUND_COLOR)
        row_to.pack(fill="x", padx=30, pady=6)
        tk.Label(
            row_to, text="To:", width=6, anchor="w",
            bg=BACKGROUND_COLOR, font=("Helvetica", 11, "bold"),
        ).pack(side="left")
        self.to_box = ttk.Combobox(row_to, values=values, state="readonly")
        self.to_box.set(values[2])  # GBP - Pound Sterling
        self.to_box.pack(side="left", fill="x", expand=True)
 
    def _build_buttons(self):
        row = tk.Frame(self.root, bg=BACKGROUND_COLOR)
        row.pack(pady=16)
 
        self.clear_button = tk.Button(
            row, text="Clear", width=12, command=self.on_clear_clicked,
            relief="groove",
        )
        self.clear_button.pack(side="left", padx=8)
 
        self.calculate_button = tk.Button(
            row, text="Calculate", width=12, command=self.on_calculate_clicked,
            relief="groove", bg=ACCENT_COLOR, fg="white",
            activebackground="#264c50", activeforeground="white",
        )
        self.calculate_button.pack(side="left", padx=8)
 
    def _build_answer_panel(self):
        panel = tk.Frame(
            self.root, bg=ANSWER_BG, highlightbackground="#cccccc",
            highlightthickness=1,
        )
        panel.pack(fill="both", expand=True, padx=20, pady=(4, 20))
 
        tk.Label(
            panel, text="Answer:", bg=ANSWER_BG, anchor="w",
            font=("Helvetica", 11, "bold"),
        ).pack(fill="x", padx=12, pady=(10, 4))
 
        self.answer_main = tk.Label(
            panel, text="", bg=ANSWER_BG, font=("Helvetica", 13, "bold"),
        )
        self.answer_main.pack(pady=(10, 4))
 
        self.answer_rate_1 = tk.Label(
            panel, text="", bg=ANSWER_BG, fg="#666666", font=("Helvetica", 10, "italic"),
        )
        self.answer_rate_1.pack()
 
        self.answer_rate_2 = tk.Label(
            panel, text="", bg=ANSWER_BG, fg="#666666", font=("Helvetica", 10, "italic"),
        )
        self.answer_rate_2.pack()
 
    # ------------------------------------------------------------------
    # Event handlers
    # ------------------------------------------------------------------
    def on_clear_clicked(self):
        self.amount_entry.delete(0, tk.END)
        self.amount_entry.insert(0, "100")
        self.from_box.set(dropdown_values()[0])
        self.to_box.set(dropdown_values()[2])
        self.answer_main.config(text="")
        self.answer_rate_1.config(text="")
        self.answer_rate_2.config(text="")
 
    def on_calculate_clicked(self):
        amount_text = self.amount_entry.get().strip()
        from_currency = code_from_dropdown(self.from_box.get())
        to_currency = code_from_dropdown(self.to_box.get())
 
        if not is_valid_amount(amount_text):
            messagebox.showerror("Invalid amount", "Please enter a positive number.")
            return
 
        if not is_valid_currency_name(from_currency) or not is_valid_currency_name(to_currency):
            messagebox.showerror("Invalid currency", "Please choose valid currencies.")
            return
 
        amount = float(amount_text)
 
        self.calculate_button.config(state="disabled", text="Calculating...")
        self.answer_main.config(text="")
        self.answer_rate_1.config(text="")
        self.answer_rate_2.config(text="")
 
        thread = threading.Thread(
            target=self._do_conversion, args=(amount, from_currency, to_currency)
        )
        thread.start()
 
    def _do_conversion(self, amount, from_currency, to_currency):
        try:
            converted_amount, rate = convert(amount, from_currency, to_currency)
            # Also compute the reverse rate for the second line, e.g.
            # "1 GBP = 1.2235 USD", to match the two-line answer style.
            reverse_rate = 1 / rate if rate else 0
            self.root.after(
                0, self._show_result, amount, from_currency,
                converted_amount, to_currency, rate, reverse_rate, None,
            )
        except ValueError as error:
            self.root.after(0, self._show_result, None, None, None, None, None, None, str(error))
 
    def _show_result(self, amount, from_currency, converted_amount, to_currency, rate, reverse_rate, error):
        self.calculate_button.config(state="normal", text="Calculate")
 
        if error:
            messagebox.showerror("Conversion failed", error)
            return
 
        self.answer_main.config(
            text=f"{amount:,.2f} {from_currency} = {converted_amount:,.2f} {to_currency}"
        )
        self.answer_rate_1.config(text=f"1 {from_currency} = {rate:.4f} {to_currency}")
        self.answer_rate_2.config(text=f"1 {to_currency} = {reverse_rate:.4f} {from_currency}")
 
    def show_currency_key(self):
        """Popup listing the currency codes and their full names."""
        popup = tk.Toplevel(self.root)
        popup.title("Currency Key")
        popup.geometry("280x360")
        popup.configure(bg=BACKGROUND_COLOR)
        popup.resizable(False, False)
 
        tk.Label(
            popup, text="Currency Key", bg=BACKGROUND_COLOR,
            font=("Helvetica", 13, "bold"),
        ).pack(pady=(12, 8))
 
        list_frame = tk.Frame(popup, bg=BACKGROUND_COLOR)
        list_frame.pack(fill="both", expand=True, padx=16, pady=(0, 12))
 
        for code, name in CURRENCY_NAMES.items():
            tk.Label(
                list_frame, text=f"{code} — {name}", bg=BACKGROUND_COLOR,
                anchor="w", font=("Helvetica", 10),
            ).pack(fill="x")

 

 
def run():
    root = tk.Tk()
    CurrencyConverterApp(root)
    root.mainloop()
 
 
if __name__ == "__main__":
    run()