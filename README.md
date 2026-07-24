# Currency Converter

A simple command-line currency converter written in Python. It fetches live exchange rates from the **Frankfurter API** and converts between currencies using a clean, modular project structure. The project is designed to demonstrate good Python programming practices while remaining easy for beginners to understand.

---

## Features

* 🌍 Live exchange rates from the Frankfurter API
* 💱 Convert between supported world currencies
* 🧩 Modular, easy-to-read codebase
* ✅ Input validation for user entries
* ⚠️ Graceful handling of common errors
* 📚 Beginner-friendly project structure

---

## Project Structure

```text
currency_converter/
├── main.py         # Entry point – handles user interaction
├── converter.py    # Core conversion logic
├── api.py          # Fetches exchange rates from the API
├── utils.py        # Helper functions (validation & formatting)
└── README.md       # Project documentation
```

Each file has a single responsibility, following the principle of **separation of concerns**.

* **main.py** handles user input and output.
* **converter.py** performs the conversion logic.
* **api.py** communicates with the exchange rate API.
* **utils.py** contains reusable helper functions with no dependencies on the other modules.

This structure keeps the code organized, reusable, and easier to maintain.

---

## Requirements

* Python 3.7 or later
* `requests`

---

## Installation

Clone the repository and install the required dependency.

```bash
git clone https://github.com/sayani-code/Currency-Converter.git
cd currency_converter
pip install requests
```

---

## How to Run

Start the application by running:

```bash
python main.py
```

You'll be prompted to enter:

1. The amount to convert
2. The source currency (e.g. `USD`)
3. The target currency (e.g. `EUR`)

Example:

```text
----------------------------------------
 Currency Converter
----------------------------------------
Tip: Use 3-letter currency codes like USD, EUR, GBP, JPY, INR.

Enter the amount to convert: 100
Convert FROM which currency? USD
Convert TO which currency? EUR

Fetching the latest exchange rate...

100.00 USD = 92.30 EUR
(1 USD = 0.9230 EUR)
```

---

## Supported Currencies

The application supports every currency available through the **Frankfurter API**, including:

* USD
* EUR
* GBP
* INR
* JPY


...and many more.

---

## Exchange Rate Source

This project uses the **Frankfurter API**, a free exchange rate API that requires **no API key or account**. It's an excellent choice for learning because you can start building immediately without additional setup.

Learn more at:

https://www.frankfurter.app/

---

## Error Handling

The application is designed to handle common issues, including:

* Invalid currency codes
* Invalid numeric input
* Network connection problems
* API service errors

Meaningful error messages are displayed to help users understand what went wrong.

---

## Learning Goals

This project demonstrates several important Python concepts:

* Modular programming
* Separation of concerns
* Functions
* API requests with `requests`
* Input validation
* Error handling
* Clean project organization

---

## Ideas for Future Improvements

Once you're comfortable with the basics, try extending the project by adding:

* Command-line arguments using `argparse`
* Exchange rate caching
* Unit tests with `pytest`
* A graphical interface using `tkinter`
* Historical exchange rate support
* Support for converting multiple amounts in one session
* Saving conversion history to a file

---

## Why This Structure?

This project follows common practices used in real-world Python applications.

* Keep user interaction separate from business logic.
* Keep network requests separate from calculations.
* Write reusable helper functions.
* Organize code so individual modules are easy to understand and test.

Following these principles makes the project easier to maintain, test, and extend.

---

## License

This project is licensed under the **MIT License**. Feel free to use, modify, and share it for learning or personal projects.

---

## Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository, open an issue, or submit a pull request.

---

## Acknowledgements

* Python
* Requests
* Frankfurter API

---

Happy coding! 🚀
