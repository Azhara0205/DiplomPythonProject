import pytest
from utils.discord_api_client import DiscordAPIClient

class TestEditMessage:
    @pytest.fixture(scope="module")
    def api_client(self):
        return DiscordAPIClient()

    def test_edit_message(self, api_client):
        channel_id = "1286673450064412684"
        message_id = "1300467508624625685"
        new_content = "This is the updated message content."
        response = api_client.edit_message(channel_id, message_id, new_content)
        assert response.status_code == 200

    def test_edit_nonexistent_message(self, api_client):
        channel_id = "1286673450064412684"
        message_id = "123456789012345678525853"
        new_content = "Updated message"
        response = api_client.edit_message(channel_id, message_id, new_content)
        assert response.status_code == 400 or 404

