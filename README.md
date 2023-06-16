# NSFW GIF Bomber Webhook

This script is designed to send NSFW (Not Safe for Work) GIFs to a Discord webhook using the Purrbot API. It utilizes the `aiohttp` library for asynchronous HTTP requests and `asyncio` for concurrent execution.

## Prerequisites
- Python 3.x
- `aiohttp` library (can be installed via `pip install aiohttp`)

## Usage
1. Make sure you have Python 3.x installed on your system.
2. Install the `aiohttp` library by running `pip install aiohttp` in your terminal.
3. Replace the `webhook_url` variable with the URL of your Discord webhook.
4. Run the script using the command `python script.py`.

## Configuration
- `base_url`: The base URL of the Purrbot API.
- `urls`: A list of specific NSFW GIF endpoints provided by the Purrbot API.
- `webhook_url`: The URL of your Discord webhook where the GIFs will be sent.

## Functionality
1. The script iterates through each URL in the `urls` list.
2. It sends an HTTP GET request to the Purrbot API for each URL to retrieve a list of NSFW GIF links.
3. For each GIF link, it sends an HTTP POST request to the specified Discord webhook, sending the GIF link as JSON payload.
4. The script logs the status of each message sent to the webhook.

Please note that this script deals with NSFW content, and you should use it responsibly and in accordance with the rules and guidelines of the platforms you are working with.
