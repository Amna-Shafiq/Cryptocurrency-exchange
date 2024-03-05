SafePay Project
This project aims to provide exchange rate information for Bitcoin and Coinbase exchanges using public APIs.

Getting Started
Follow these instructions to set up and run the project locally on your machine.

Prerequisites
Python 3.x
Pip
Installation
Clone the repository:

bash
Copy code
git clone <repository-url>
Navigate to the project directory:

bash
Copy code
cd SafePay\Backend\safepayproject
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Running the Project
Start the Django development server:

bash
Copy code
python manage.py runserver
Access the project in your web browser at http://127.0.0.1:8000/.

Running Tests
To run the test suite, execute the following command:

bash
Copy code
python manage.py test CryptocurrencyExchange.tests
Usage
Access the exchange rate API endpoint at /exchange-routing/ with the amount parameter specifying the amount in USD.

Example:

bash
Copy code
http://127.0.0.1:8000/exchange-routing/?amount=1
Service Details
The service to hit APIs and find the lowest price is implemented inside the services folder. This service interacts with the public APIs of Bitcoin and Coinbase exchanges using the requests library in Python.