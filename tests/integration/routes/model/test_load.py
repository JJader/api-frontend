from fastapi.testclient import TestClient
from main import app
import pytest
from io import BytesIO

client = TestClient(app)


@pytest.fixture
def mock_load_task(mocker):
    return mocker.patch("routes.model.load.app", autospec=True)


def test_read_load(mock_load_task):

    model_name = "test_model"
    flavor = "test_flavor"

    file_content = b"dummy file content"
    file = ("test_file.pkl", BytesIO(file_content), "application/octet-stream")

    response = client.post(
        "/model/load",
        params={"model_name": model_name, "flavor": flavor},
        files={"file": file},
    )

    assert response.status_code == 200
    assert response.json() == {"task_id": {}}
