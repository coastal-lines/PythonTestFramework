import pytest


@pytest.mark.parametrize("kucoin_service", [{"url":"https://api.kucoin.com/", "end_point":"api/v1/bullet-public"}], indirect=True)
def test_validate_public_token_response(kucoin_service):
    assert kucoin_service.code == "200000"

    assert kucoin_service.data.token is not None
    assert len(kucoin_service.data.token) > 150

    assert kucoin_service.data.instanceServers[0].endpoint == "wss://ws-api-spot.kucoin.com/"
    assert kucoin_service.data.instanceServers[0].encrypt == True
    assert kucoin_service.data.instanceServers[0].protocol == "websocket"
    assert kucoin_service.data.instanceServers[0].pingInterval == 18000
    assert kucoin_service.data.instanceServers[0].pingTimeout == 10000

