# SafePay Project

This project aims to provide exchange rate information for Binance and Coinbase exchanges using public APIs.

## Getting Started

Follow these instructions to set up and run the project locally on your machine.

### Prerequisites

- Python 3.x
- Pip

### Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd SafePay\Backend\safepayproject
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Project

1. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

2. Access the project in your web browser at [http://127.0.0.1:8000/exchange-routing/?amount=1](http://127.0.0.1:8000/exchange-routing/?amount=1).

## Running Tests

To run the test suite, execute the following command:

```bash
python manage.py test CryptocurrencyExchange.tests
 ```


## Usage
Access the exchange rate API endpoint at /exchange-routing/ with the amount parameter specifying the amount in USD.

Example:

http://127.0.0.1:8000/exchange-routing/?amount=1

## Service Details 
The service to hit APIs and find the lowest price is implemented inside the services folder. This service interacts with the public APIs of Binance and Coinbase exchanges using the requests library in Python.