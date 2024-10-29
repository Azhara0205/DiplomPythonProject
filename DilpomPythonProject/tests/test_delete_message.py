import pytest
from utils.discord_api_client import DiscordAPIClient

class TestDeleteMessage:
    @pytest.fixture(scope="module")
    def api_client(self):
        return DiscordAPIClient()

    def test_delete_message(self, api_client):
        channel_id = "1286673450064412684"
        message_id = "1299352610465120257"
        response = api_client.delete_message(channel_id, message_id)
        assert response.status_code == 204

    def test_delete_nonexistent_message(self, api_client):
        channel_id = "1286673450064412684"
        message_id = "123456789012345678"
        response = api_client.delete_message(channel_id, message_id)
        assert response.status_code == 404 or 404

    def test_delete_message_from_nonexistent_channel(self, api_client):
        channel_id = "123456789012345678"
        message_id = "987654321098765432"
        response = api_client.delete_message(channel_id, message_id)
        assert response.status_code == 404 or 400


