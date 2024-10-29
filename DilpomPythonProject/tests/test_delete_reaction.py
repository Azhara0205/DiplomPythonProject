import pytest
from utils.discord_api_client import DiscordAPIClient

class TestDeleteReaction:
    @pytest.fixture(scope="module")
    def api_client(self):
        return DiscordAPIClient()

    def test_remove_reaction(self, api_client):
        channel_id = "1286673450064412684"
        message_id = "1300467508624625685"
        emoji = "👍"
        response = api_client.remove_reaction(channel_id, message_id, emoji)
        assert response.status_code == 204

    def test_remove_reaction_from_nonexistent_message(self, api_client):
        channel_id = "1286673450064412684"
        message_id = "7858757"
        emoji = "👍"
        response = api_client.remove_reaction(channel_id, message_id, emoji)
        assert response.status_code == 404

    def test_remove_invalid_reaction(self, api_client):
        channel_id = "1286673450064412684"
        message_id = "1300467508624625685"
        emoji = "!@#$%^&*()"
        response = api_client.remove_reaction(channel_id, message_id, emoji)
        assert response.status_code == 400