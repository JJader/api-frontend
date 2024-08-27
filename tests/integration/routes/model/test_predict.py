from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)


@pytest.fixture
def mock_send_task(mocker):
    return mocker.patch("routes.model.predict.app", autospec=True)


def test_read_predict(mock_send_task):
    payload = {"model_name": "test_input", "data": {}}

    response = client.post("/model/predict", json=payload)

    assert response.status_code == 200
    assert response.json() == {"result": {}, "metadata": {}}
