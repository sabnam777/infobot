# Telegram Bot

[![License](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)

A Telegram bot that allows users to access premium content, donate, and join group/channel.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Home page with three buttons: top, bottom, and last format
- Two buttons to redirect users to group/channel
- Premium button that leads to a new page with an image and a quote to buy premium
- Donation button with an image, donation quotes, and Paytm, UPI, Phone Pay buttons
- Broadcast feature for owner only

## Requirements

- Python 3.7+
- MongoDB
- Telegram API Key

## Installation

1. Clone this repository:
`git clone https://github.com/yourusername/telegram-bot.git`

2. Create a virtual environment and activate it:
`python3 -m venv venv
source venv/bin/activate`

3. Install the required packages:
`pip install -r requirements.txt`


4. Create a `config.py` file and add your Telegram API key and MongoDB URL:
`API_KEY = "your_telegram_api_key"
MONGO_URL = "your_mongodb_url`

## Usage

1. Run the bot:
`python main.py`


2. Open the Telegram app and search for your bot. Send a message to start interacting with it.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
You can customize it further to match the style and content of your project.
