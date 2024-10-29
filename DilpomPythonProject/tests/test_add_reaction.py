import pytest
from utils.discord_api_client import DiscordAPIClient

class TestAddReaction:
    @pytest.fixture(scope="module")
    def api_client(self):
        return DiscordAPIClient()

    def test_add_reaction(self, api_client):
        channel_id = "1286673450064412684"
        message_id = "1300467508624625685"
        emoji = "👍"
        response = api_client.add_reaction(channel_id, message_id, emoji)
        assert response.status_code == 204

    def test_add_reaction_to_nonexistent_message(self, api_client):
        channel_id = "1286673450064412684"
        message_id = "1234567890123456742527"
        emoji = "👍"
        response = api_client.add_reaction(channel_id, message_id, emoji)
        assert response.status_code == 404 or 400

    def test_add_invalid_reaction(self, api_client):
        channel_id = "1286673450064412684"
        message_id = "1300467508624625685"
        emoji = "!@#$%^&*()"
        response = api_client.add_reaction(channel_id, message_id, emoji)
        assert response.status_code == 400 or 404