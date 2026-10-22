# Caderno de Erros

Anotacoes dos erros que encontrei nos exercicios, o que quebrou e como resolvi.

Autor: ThyagoToledo

---

## 13/10/2026 - Dia 01

### Git - Permissao no pendrive (safe.directory)
- Onde foi: Terminal ao rodar git add no pendrive F:\backend-estudos.
- Erro: fatal: detected dubious ownership in repository at 'F:/backend-estudos'.
- O que eu esperava: Adicionar os arquivos normalmente para commitar.
- Causa: O pendrive esta formatado em FAT32/exFAT e nao grava permissoes de usuario do Windows (NTFS). O Git acha que a pasta pode pertencer a outro usuario e bloqueia por seguranca.
- Solucao: Rodei git config --global --add safe.directory F:/backend-estudos.
- Licao: No Windows, sempre que usar repositorio em pendrive ou disco externo, preciso liberar a pasta no Git antes de rodar qualquer comando.

---

## 15/10/2026 - Dia 02

### Python - Erro ao converter texto em numero (ValueError)
- Onde foi: semana-01/perfil.py (Exercicio N3).
- Erro: ValueError: invalid literal for int() with base 10: 'abc'.
- O que eu esperava: O exercicio pediu de proposito para passar 'abc' no campo de ano para ver o que acontecia.
- Causa: A funcao int() so converte digitos numericos de 0 a 9. Ao receber texto, o Python lanca ValueError e interrompe o script na mesma hora.
- Solucao: Entendi o erro e anotei. No Dia 06 vamos aprender a tratar com try/except para a aplicacao nao cair se o usuario digitar errado.
- Licao: input() sempre devolve string. Fazer int(input()) direto sem tratar a entrada pode quebrar o programa facilmente.

### Python - Usuario digitando nota com virgula
- Onde foi: semana-01/d02_perfil.py (Desafio N4 da media).
- Erro: ValueError: could not convert string to float: '8,5'.
- O que eu esperava: Aceitar notas no padrao brasileiro (com virgula) e calcular a media com 2 casas.
- Causa: O Python segue o padrao americano que usa ponto (.) para separar decimais. O float() nao reconhece a virgula.
- Solucao: Tratei a string antes da conversao trocando virgula por ponto com .replace(',', '.').
- Licao: No Brasil a maioria das pessoas digita decimal com virgula. Sempre que receber dados numericos do usuario preciso normalizar antes de converter para float.
