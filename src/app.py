"""MedTrack - Controle de Medicamentos para Idosos (CLI)."""

import argparse
import sys

from .storage import Storage

storage = Storage()


def cmd_adicionar(args: argparse.Namespace) -> None:
    """Adiciona um medicamento ao controle."""
    med = storage.adicionar(
        nome=args.nome,
        horario=args.horario,
        dose=args.dose,
    )
    print(f"✅ Medicamento '{med['nome']}' adicionado (ID {med['id']}).")


def cmd_listar(args: argparse.Namespace) -> None:  # noqa: ARG001
    """Lista todos os medicamentos cadastrados."""
    meds = storage.listar()
    if not meds:
        print("Nenhum medicamento cadastrado.")
        return
    print(f"\n{'ID':<5} {'Nome':<25} {'Horário':<10} {'Dose':<15} {'Tomado?'}")
    print("-" * 65)
    for m in meds:
        tomado = "✅ Sim" if m.get("tomado") else "❌ Não"
        print(f"{m['id']:<5} {m['nome']:<25} {m['horario']:<10} {m['dose']:<15} {tomado}")


def cmd_tomar(args: argparse.Namespace) -> None:
    """Marca um medicamento como tomado."""
    med = storage.marcar_tomado(args.id)
    if med is None:
        print(f"❌ Medicamento com ID {args.id} não encontrado.")
        sys.exit(1)
    print(f"✅ '{med['nome']}' marcado como tomado.")


def cmd_remover(args: argparse.Namespace) -> None:
    """Remove um medicamento pelo ID."""
    removido = storage.remover(args.id)
    if not removido:
        print(f"❌ Medicamento com ID {args.id} não encontrado.")
        sys.exit(1)
    print(f"✅ Medicamento ID {args.id} removido com sucesso.")


def cmd_resetar(args: argparse.Namespace) -> None:  # noqa: ARG001
    """Reseta o status 'tomado' de todos os medicamentos (novo dia)."""
    storage.resetar_dia()
    print("🔄 Status de todos os medicamentos resetado para o novo dia.")


def build_parser() -> argparse.ArgumentParser:
    """Constrói e retorna o parser da CLI."""
    parser = argparse.ArgumentParser(
        prog="medtrack",
        description="MedTrack — Controle de Medicamentos para Idosos",
    )
    sub = parser.add_subparsers(dest="comando", required=True)

    # adicionar
    p_add = sub.add_parser("adicionar", help="Adiciona um medicamento")
    p_add.add_argument("--nome", required=True, help="Nome do medicamento")
    p_add.add_argument("--horario", required=True, help="Horário (ex: 08:00)")
    p_add.add_argument("--dose", required=True, help="Dose (ex: 1 comprimido)")
    p_add.set_defaults(func=cmd_adicionar)

    # listar
    p_list = sub.add_parser("listar", help="Lista todos os medicamentos")
    p_list.set_defaults(func=cmd_listar)

    # tomar
    p_take = sub.add_parser("tomar", help="Marca medicamento como tomado")
    p_take.add_argument("id", type=int, help="ID do medicamento")
    p_take.set_defaults(func=cmd_tomar)

    # remover
    p_rem = sub.add_parser("remover", help="Remove um medicamento")
    p_rem.add_argument("id", type=int, help="ID do medicamento")
    p_rem.set_defaults(func=cmd_remover)

    # resetar
    p_reset = sub.add_parser("resetar", help="Reseta status para novo dia")
    p_reset.set_defaults(func=cmd_resetar)

    return parser


def main() -> None:
    """Ponto de entrada principal."""
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
