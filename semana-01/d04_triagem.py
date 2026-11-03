# Arquivo: d04_triagem.py | Data: 30/10/2026

# Triagem de tarefas (regras de negocio)
prioridade = int(input("Prioridade (1 a 3): "))
concluida = input("Concluida (s/n): ")
prazo_em_dias = int(input("Prazo em dias: "))

# Logica de decisao
if concluida == "s":
    print("Concluída: arquivar")
elif prioridade == 1 and prazo_em_dias <= 1:
    print("URGENTE: fazer hoje")
elif prioridade == 1:
    print("Importante: agendar esta semana")
elif prazo_em_dias <= 0:
    print("Atrasada: renegociar prazo")
else:
    print("Pode esperar")
    