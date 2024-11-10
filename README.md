# 🤖 Nuru Bot

Welcome to the **Nuru Bot**, your friendly virtual assistant powered by AI technology. This bot is designed to provide instant support, answer questions, and engage users in meaningful conversations all within the convenience of Telegram.

## 🌟 Features

- **Intelligent Conversations**: Harnesses the power of OpenAI's GPT model to deliver human-like responses.
- **User friendly Commands**: Simple commands to guide users through interactions.
- **Real-Time Engagement**: Responds instantly to user inquiries, making it perfect for support scenarios.

## 🚀 Getting Started

Follow these steps to set up your bot.

### Prerequisites

Before diving in make sure you have:

- Python 3.10 or higher installed on your machine.
- A Telegram account to create and interact with your bot.
- An OpenAI API key for accessing the AI model.

### Installation Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Ombito/Nuru-Bot.git
   cd Nuru-Bot

2. **Install Required Libraries**:
    Install the necessary Python packages using pip:
    
    ```bash
    pip install python-telegram-bot openai python-dotenv

3. **Configure Environment Variables**:
    Create a .env file in the project directory and add your credentials:
    
    ```text
    TOKEN='your_telegram_bot_token'
    OPENAI_API_KEY='your_openai_api_key'
- Replace your_telegram_bot_token with the token you received from BotFather.
- Replace your_openai_api_key with your OpenAI API key from OpenAI.

## 🛠️ Usage
1. Start Your Bot:
    Launch the bot by running the following command in your terminal:
    ```bash
    cd app
    python main.py

2. Engage with Your Bot:
    - Open Telegram and search for your bot using its username.
    - Begin chatting. Use commands like /start or /help to learn more about what the bot can do.
    - Ask any question or send a message and watch as the bot responds with AI-generated insights.


## 📜 Available Commands
Here’s a quick overview of commands you can use with the bot:

    /start: Kick off your interaction with a warm welcome message.
    /help: Get a list of available commands and tips on how to use them.
    Just type your questions directly no commands needed.

## 🔍 Code Structure
The project is organized as follows:

    main.py: The core script that runs the Telegram bot.
    .env: Configuration file for storing sensitive information like API keys.
    Pipfile: A file that defines dependencies for managing packages using Pipenv
    requirements.txt: A list of required Python packages.


## 🤝 Contributing
We welcome contributions from everyone. If you have ideas for new features or improvements here is how you can help:
1. Fork the repository.
2. Create a feature branch (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -m 'Add some AmazingFeature').
4. Push to your branch (git push origin feature/AmazingFeature).
5. Open a pull request.
   

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.


## 🙏 Acknowledgments
- A huge thank you to OpenAI for providing powerful AI models that make this bot possible.
- Special thanks to python-telegram-bot for their excellent library that simplifies Telegram bot development.