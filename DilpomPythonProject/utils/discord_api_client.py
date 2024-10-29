import requests
import os
from dotenv import load_dotenv

class DiscordAPIClient:
    def __init__(self):
        load_dotenv()  # Загружаем переменные окружения из .env файла
        self.base_url = "https://discord.com/api/v10"
        self.token = os.getenv("DISCORD_TOKEN")  # Получаем токен из переменной окружения

    def send_message(self, channel_id, message_content):
        url = f"{self.base_url}/channels/{channel_id}/messages"
        headers = {
            "Authorization": f"Bot {self.token}",
            "Content-Type": "application/json",
        }
        payload = {
            "content": message_content,
        }
        response = requests.post(url, headers=headers, json=payload)
        return response

    def delete_message(self, channel_id, message_id):
        url = f"{self.base_url}/channels/{channel_id}/messages/{message_id}"
        headers = {
            "Authorization": f"Bot {self.token}",
        }
        response = requests.delete(url, headers=headers)
        return response

    def edit_message(self, channel_id, message_id, new_content):
        url = f"{self.base_url}/channels/{channel_id}/messages/{message_id}"
        headers = {
            "Authorization": f"Bot {self.token}",
            "Content-Type": "application/json",
        }
        payload = {
            "content": new_content,
        }
        response = requests.patch(url, headers=headers, json=payload)
        return response

    def add_reaction(self, channel_id, message_id, emoji):
        url = f"{self.base_url}/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me"
        headers = {
            "Authorization": f"Bot {self.token}",
        }
        response = requests.put(url, headers=headers)
        return response

    def remove_reaction(self, channel_id, message_id, emoji):
        url = f"{self.base_url}/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me"
        headers = {
            "Authorization": f"Bot {self.token}",
        }
        response = requests.delete(url, headers=headers)
        return response
