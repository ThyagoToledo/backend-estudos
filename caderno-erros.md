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

---

## 16/10/2026 - Dia 03

### Python - Divisao por zero (ZeroDivisionError)
- Onde foi: semana-01/d03_operadores.py (Tabela de operacoes com a e b).
- Erro: ZeroDivisionError: division by zero.
- O que eu esperava: O exercicio pediu de proposito para passar b = 0 nos testes para observar a quebra.
- Causa: Nao existe divisao por zero na matematica. Quando b vale 0, qualquer tentativa de divisao real (/), inteira (//) ou resto (%) lanca ZeroDivisionError e para o programa imediatamente.
- Solucao: Anotei a ocorrencia do erro conforme solicitado pelo plano. No Dia 06 vamos implementar validacao de entrada antes do calculo.
- Licao: Em qualquer endpoint ou logica de BackEnd que envolva calculo de divisao, nunca posso confiar cegamente que o denominador e maior que zero; a checagem previa e obrigatoria.

---

## 03/11/2026 - Dia 04

### Python - Ordem das condicoes em if e elif
- Onde foi: semana-01/d04_triagem.py (Logica de triagem de prioridades e prazos).
- Erro: Um elif mais generico captura o fluxo antes de um elif mais especifico se a ordem for invertida.
- O que eu esperava: Que a prioridade 1 com prazo <= 1 fosse marcada como urgente (fazer hoje), mas se prioridade 1 geral viesse antes, a condicao mais especifica nunca seria atingida.
- Causa: O interpretador Python entra no primeiro bloco cuja expressao for verdadeira e pula os demais. Se a condicao ampla vier primeiro, o caso especifico vira codigo morto.
- Solucao: Ordenei os testes sempre do mais urgente e restrito para o mais generico (concluida primeiro, depois prioridade 1 com prazo curto, depois prioridade 1 geral).
- Licao: Em regras de negocio com multiplas faixas e condicoes encadeadas, a ordem de checagem define o comportamento correto da aplicacao.
