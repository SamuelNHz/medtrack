# Changelog

Todas as mudanças notáveis neste projeto serão documentadas aqui.

## [1.0.0] - 2026-04-12

### Adicionado
- Comando `adicionar` para cadastrar medicamentos com nome, horário e dose
- Comando `listar` para visualizar todos os medicamentos e seu status
- Comando `tomar` para marcar um medicamento como tomado no dia
- Comando `remover` para excluir um medicamento do controle
- Comando `resetar` para reiniciar o status diário de todos os medicamentos
- Persistência de dados em arquivo JSON local
- Testes automatizados com pytest cobrindo 11 cenários
- Linting configurado com Ruff
- Pipeline de CI com GitHub Actions
