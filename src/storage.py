"""Módulo de persistência de dados em arquivo JSON."""

import json
from pathlib import Path
from typing import Optional


class Storage:
    """Gerencia o armazenamento de medicamentos em um arquivo JSON."""

    def __init__(self, filepath: str = "medicamentos.json") -> None:
        self.filepath = Path(filepath)
        self._dados: dict = self._carregar()

    def _carregar(self) -> dict:
        if self.filepath.exists():
            with self.filepath.open(encoding="utf-8") as f:
                return json.load(f)
        return {"proximo_id": 1, "medicamentos": []}

    def _salvar(self) -> None:
        with self.filepath.open("w", encoding="utf-8") as f:
            json.dump(self._dados, f, ensure_ascii=False, indent=2)

    def adicionar(self, nome: str, horario: str, dose: str) -> dict:
        """Adiciona um novo medicamento e retorna o registro criado."""
        if not nome or not nome.strip():
            raise ValueError("Nome do medicamento não pode ser vazio.")
        if not horario or not horario.strip():
            raise ValueError("Horário não pode ser vazio.")
        if not dose or not dose.strip():
            raise ValueError("Dose não pode ser vazia.")

        med = {
            "id": self._dados["proximo_id"],
            "nome": nome.strip(),
            "horario": horario.strip(),
            "dose": dose.strip(),
            "tomado": False,
        }
        self._dados["medicamentos"].append(med)
        self._dados["proximo_id"] += 1
        self._salvar()
        return med

    def listar(self) -> list:
        """Retorna a lista de todos os medicamentos."""
        return self._dados["medicamentos"]

    def buscar_por_id(self, med_id: int) -> Optional[dict]:
        """Busca um medicamento pelo ID."""
        for med in self._dados["medicamentos"]:
            if med["id"] == med_id:
                return med
        return None

    def marcar_tomado(self, med_id: int) -> Optional[dict]:
        """Marca um medicamento como tomado. Retorna o registro ou None."""
        med = self.buscar_por_id(med_id)
        if med is None:
            return None
        med["tomado"] = True
        self._salvar()
        return med

    def remover(self, med_id: int) -> bool:
        """Remove um medicamento pelo ID. Retorna True se removido."""
        antes = len(self._dados["medicamentos"])
        self._dados["medicamentos"] = [
            m for m in self._dados["medicamentos"] if m["id"] != med_id
        ]
        if len(self._dados["medicamentos"]) < antes:
            self._salvar()
            return True
        return False

    def resetar_dia(self) -> None:
        """Reseta o campo 'tomado' de todos os medicamentos."""
        for med in self._dados["medicamentos"]:
            med["tomado"] = False
        self._salvar()
