import pytest
from unittest.mock import MagicMock
from infra.firestore_repo import FirestoreTemporadaRepo

def test_create_and_get_temporada():
    mock_db = MagicMock()
    repo = FirestoreTemporadaRepo(mock_db)

    mock_doc = MagicMock()
    mock_doc.id = "temp123"
    mock_db.collection().document.return_value = mock_doc

    temporada_id = repo.create_temporada({"nome": "Temporada 1", "ativa": True})
    assert temporada_id == "temp123"
    mock_db.collection().document().set.assert_called_once()
