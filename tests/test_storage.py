"""Testes automatizados para o MedTrack."""

import pytest

from src.storage import Storage


@pytest.fixture
def storage(tmp_path):
    """Cria uma instância de Storage isolada para cada teste."""
    return Storage(filepath=str(tmp_path / "test_meds.json"))


# --- Testes de adição ---

def test_adicionar_medicamento_valido(storage):
    """Caminho feliz: adiciona um medicamento com dados corretos."""
    med = storage.adicionar(nome="Paracetamol", horario="08:00", dose="500mg")
    assert med["nome"] == "Paracetamol"
    assert med["horario"] == "08:00"
    assert med["dose"] == "500mg"
    assert med["tomado"] is False
    assert med["id"] == 1


def test_adicionar_multiplos_medicamentos(storage):
    """Adicionar vários medicamentos gera IDs sequenciais."""
    storage.adicionar("Aspirina", "07:00", "100mg")
    storage.adicionar("Rivotril", "22:00", "0,5mg")
    meds = storage.listar()
    assert len(meds) == 2
    assert meds[0]["id"] == 1
    assert meds[1]["id"] == 2


def test_adicionar_nome_vazio_levanta_erro(storage):
    """Entrada inválida: nome vazio deve lançar ValueError."""
    with pytest.raises(ValueError, match="Nome"):
        storage.adicionar(nome="", horario="08:00", dose="1 comprimido")


def test_adicionar_horario_vazio_levanta_erro(storage):
    """Entrada inválida: horário vazio deve lançar ValueError."""
    with pytest.raises(ValueError, match="Horário"):
        storage.adicionar(nome="Omeprazol", horario="", dose="20mg")


def test_adicionar_dose_vazia_levanta_erro(storage):
    """Entrada inválida: dose vazia deve lançar ValueError."""
    with pytest.raises(ValueError, match="Dose"):
        storage.adicionar(nome="Omeprazol", horario="12:00", dose="")


# --- Testes de listagem ---

def test_listar_vazio(storage):
    """Lista retorna vazia quando não há medicamentos."""
    assert storage.listar() == []


# --- Testes de marcar tomado ---

def test_marcar_tomado(storage):
    """Caminho feliz: marca medicamento existente como tomado."""
    med = storage.adicionar("Losartana", "09:00", "50mg")
    resultado = storage.marcar_tomado(med["id"])
    assert resultado is not None
    assert resultado["tomado"] is True


def test_marcar_tomado_id_inexistente(storage):
    """Caso limite: ID inexistente retorna None."""
    resultado = storage.marcar_tomado(999)
    assert resultado is None


# --- Testes de remoção ---

def test_remover_medicamento_existente(storage):
    """Caminho feliz: remove um medicamento existente."""
    med = storage.adicionar("Metformina", "12:00", "850mg")
    removido = storage.remover(med["id"])
    assert removido is True
    assert storage.listar() == []


def test_remover_id_inexistente(storage):
    """Caso limite: tentar remover ID que não existe retorna False."""
    resultado = storage.remover(999)
    assert resultado is False


# --- Testes de resetar ---

def test_resetar_dia(storage):
    """Resetar o dia muda todos os medicamentos de tomado=True para False."""
    m1 = storage.adicionar("Atenolol", "08:00", "25mg")
    m2 = storage.adicionar("AAS", "12:00", "100mg")
    storage.marcar_tomado(m1["id"])
    storage.marcar_tomado(m2["id"])

    storage.resetar_dia()
    for med in storage.listar():
        assert med["tomado"] is False
