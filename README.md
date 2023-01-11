# Yobit-Crypto-Exchange-Parser
The code is a Python script 🐍 that utilizes the YoBit crypto exchange's API 💹 to retrieve different types of information such as general information 📊, ticker information 📈📉, order book 📊, and recent trades 💰. The retrieved information is then saved to text files 📄. The code is structured as a class `YoBitAPI` which contains different methods 🔍 to get the different types of information, it also has a helper function which will help to save file to the specific location. The main function calls the methods 🔍 in order to retrieve and save the information 💾.

## Code functionality

The code defines a class `YoBitAPI` that allows to get different types of information from the YoBit crypto exchange. The class has the following methods:

- `get_info():` 
This method retrieves general information about the exchange and saves the response in a text file named `"results/info.txt"`

- `get_ticker(coin1, coin2):` 
This method retrieves the ticker information for a given pair of coins (specified by the `coin1` and `coin2` parameters) and saves the response in a text file named `"results/ticker.txt"`. By default, it retrieves the ticker information for the BTC/USD pair.

- `get_depth(coin1, coin2, limit):`
This method retrieves the order book (i.e., the bids and asks) for a given pair of coins and saves the response in a text file named `"results/depth.txt"`. By default, it retrieves the depth information for the BTC/USD pair with a limit of 150. It also return sum of bids' amount.

- `get_trades(coin1, coin2, limit):`
This method retrieves recent trades for a given pair of coins and saves the response in a text file named `"results/trades.txt"`. By default, it retrieves the trade information for the BTC/USD pair with a limit of 150. it return sum of ask trades and bid trades.

- `save_to_file(file_name, content):` 
It is a helper function which will help to save file at specific location with specific name.

The `main()` function at the end of the code creates an instance of the `YoBitAPI` class and calls some of its methods to retrieve different types of information from the exchange.

#### Technologies and Libraries
- **[Python 3.x+](https://www.python.org/)**: the main programming language that was used 
- **[requests](https://requests.readthedocs.io/en/latest/)**: a library for making HTTP requests in Python