from src.tasks.utils import get_predict_tasks, get_load_result, get_load_tasks
import pytest
from unittest.mock import MagicMock, AsyncMock
from fastapi import UploadFile, HTTPException
from contextlib import nullcontext as does_not_raise


@pytest.mark.parametrize(
    "features",
    [
        ({"feature1": 1.0, "feature2": 2.0}),
        ({}),
    ],
)
def test_get_predict_tasks(features):

    request = {"model_name": "test_model", "data": features}

    task_name, data = get_predict_tasks(request)

    expected_data = {
        "model_name": "test_model",
        "data": features,
    }

    assert data == expected_data
    assert task_name == "app.mlflow.tasks.predict"


def test_get_load_result():
    mock_result = MagicMock()
    mock_result.name = "mock_task_name"
    mock_result.task_id = "mocked_task_id"
    mock_result.result = {"key": "value"}
    mock_result.status = "completed"

    task_name, data = get_load_result(mock_result)

    expected_data = {
        "task_id": "mocked_task_id",
        "result": {"key": "value"},
        "status": "completed",
    }

    assert data == expected_data
    assert task_name == "mock_task_name"


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "filename, expected_data, raises",
    [
        (
            "model.pkl",
            {
                "data": b"file content",
                "model_name": "test_model",
                "backend": "test_flavor",
            },
            does_not_raise(),
        ),
        ("model.txt", None, pytest.raises(HTTPException)),
    ],
)
async def test_get_load_tasks(filename, expected_data, raises):

    mock_file = MagicMock(spec=UploadFile)
    mock_file.filename = filename
    mock_file.read = AsyncMock(return_value=b"file content")
    mock_file.close = AsyncMock()

    with raises:
        task_name, data = await get_load_tasks(
            model_name="test_model", flavor="test_flavor", request=mock_file
        )

        assert task_name == "app.mlflow.tasks.load"
        assert data == expected_data
        mock_file.close.assert_called_once()
