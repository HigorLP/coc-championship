import pytest
from unittest.mock import MagicMock
from infra.firestore_repo import FirestorePlayerRepo

def test_add_and_list_players():
    # mock do firestore
    mock_db = MagicMock()
    repo = FirestorePlayerRepo(mock_db)

    # adicionar jogador
    mock_doc = MagicMock()
    mock_doc.id = "123"
    mock_db.collection().document.return_value = mock_doc
    repo.add_player("Alice", "#TAG")

    mock_db.collection().document().set.assert_called_once()
