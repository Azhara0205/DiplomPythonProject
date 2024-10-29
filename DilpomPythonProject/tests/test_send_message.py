import pytest
from utils.discord_api_client import DiscordAPIClient

class TestSendMessage:
    @pytest.fixture(scope="module")
    def api_client(self):
        return DiscordAPIClient()

    def test_send_message(self, api_client):
        channel_id = "1286673450064412684"
        message_content = "Hello, this is a test message!"
        response = api_client.send_message(channel_id, message_content)
        assert response.status_code == 200

    def test_send_empty_message(self, api_client):
        channel_id = "1286673450064412684"
        response = api_client.send_message(channel_id, " ")
        assert response.status_code == 400

    def test_send_message_to_nonexistent_channel(self, api_client):
        channel_id = "123456789012345678"
        response = api_client.send_message(channel_id, "Hello!")
        assert response.status_code == 404