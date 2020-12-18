# witch

Being f̸am̨oús is optional.

Witch is a minimal Twitch bot that fights ad bots.

# Setup

Requires Python 3.6, but later versions will give more up-to-date unicode data.

## Installing

```sh
# Clone repository
git clone https://github.com/vvvvvvivi/witch.git
cd witch

# Create and activate virtual environment
python3 -m venv venv

source venv/bin/activate # Shell (Linux, macOS)
venv/Scripts/Activate    # Batch (Windows)

# Install dependencies
pip install -Ur requirements.txt
```

## Configuring

You can use environment variables in your shell, but you'll most likely want to create a file named `.env`. It should have the following format:

```
IRC_NICK=your_chat_bot
IRC_TOKEN=oauth:0123456789abcdefghijklmnopqrst
CLIENT_ID=0123456789abcdefghijklmnopqrst
```

The IRC nick and token will be used to log in to IRC. To get the token sign in with the bot account and go to <https://twitchapps.com/tmi/>.

To get a client ID, go to <https://dev.twitch.tv/console/apps/create> and create an application. The redirect URL does not matter, `http://localhost` will work fine.

Once `.env` is filled in, you now must create a `filters.json` file. It is a simple key-value object that maps channel names to a list of blocked terms. An example is given below:

```json
{
  "your_channel_name": [
    "wanna become famous",
    "the game",
    "another blocked term"
  ]
}
```

## Running

Once installed and configured, you can run the bot.

Make sure the virtual environment is still active, if it is not you can repeat the activate command from the installation step.

```sh
python bot.py
```

Keep the command running in the background to make sure your bot keeps running.
