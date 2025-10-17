import json
import os
from datetime import datetime
1
ORDENS_DE_ENTREGA = []
ARQUIVO_JSON = 'ordens_entrega.json'
ARQUIVO_LOG_TEXTO = 'log_rastreamento.txt'

def carregar_ordens():
    global ORDENS_DE_ENTREGA
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, 'r') as f:
            try:
                ORDENS_DE_ENTREGA = json.load(f)
            except json.JSONDecodeError:
                ORDENS_DE_ENTREGA = []
    else:
        ORDENS_DE_ENTREGA = []

def salvar_ordens():
    with open(ARQUIVO_JSON, 'w') as f:
        json.dump(ORDENS_DE_ENTREGA, f, indent=4)

def logar_evento(mensagem):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ARQUIVO_LOG_TEXTO, 'a') as f:
        f.write(f"[{timestamp}] {mensagem}\n")

def validar_float(mensagem):
    while True:
        try:
            valor = input(mensagem)
            return float(valor)
        except ValueError:
            print("❌ Erro: Digite um valor numérico válido.")

def calcular_previsao_chegada(horas_restantes):
    try:
        agora = datetime.now()
        from datetime import timedelta
        delta = timedelta(hours=horas_restantes)

        previsao = agora + delta
        return previsao.strftime("%Y-%m-%d %H:%M")
    except Exception:
        return "Erro de Cálculo"

def registrar_nova_ordem():
    print("\n--- Cadastro de Nova Ordem de Entrega ---")

    rota_id = input("ID da Rota (Ex: ROTA-SUD-005): ").upper()
    destino = input("Destino (Cidade/Cliente): ")

    tempo_estimado = validar_float("Tempo estimado de viagem (Horas): ")

    previsao_chegada = calcular_previsao_chegada(tempo_estimado)

    nova_ordem = {
        'id': rota_id,
        'destino': destino,
        'status': 'EM TRÂNSITO',
        'previsao': previsao_chegada,
        'log_status': [(datetime.now().strftime("%Y-%m-%d %H:%M"), 'Rota iniciada')]
    }

    ORDENS_DE_ENTREGA.append(nova_ordem)
    salvar_ordens()
    logar_evento(f"Nova rota registrada: {rota_id} para {destino}")
    print(f"✅ Ordem {rota_id} registrada. Previsão: {previsao_chegada}")

def atualizar_status():
    rota_consulta = input("ID da Rota para Atualizar: ").upper()

    for ordem in ORDENS_DE_ENTREGA:
        if ordem['id'] == rota_consulta:
            novo_status = input("Novo Status (Ex: EM TRÂNSITO, ATRASADA, ENTREGUE): ").upper()
            ordem['status'] = novo_status

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            ordem['log_status'].append((timestamp, novo_status))

            if novo_status != 'ENTREGUE':
                horas = validar_float("Novo Tempo Restante Estimado (Horas): ")
                ordem['previsao'] = calcular_previsao_chegada(horas)

            salvar_ordens()
            logar_evento(f"Status da rota {rota_consulta} atualizado para {novo_status}.")
            print(f"✅ Status da Rota {rota_consulta} atualizado com sucesso!")
            return

    print(f"❌ Rota {rota_consulta} não encontrada.")


def rastrear_ordem():

    rota_consulta = input("\nDigite o ID da Rota para Rastrear: ").upper()

    ordem_encontrada = None
    for ordem in ORDENS_DE_ENTREGA:
        if ordem['id'] == rota_consulta:
            ordem_encontrada = ordem
            break

    print("\n--- Painel de Rastreamento da AgroRota ---")
    if ordem_encontrada:
        print(f"ID da Rota: {ordem_encontrada['id']}")
        print(f"Destino: {ordem_encontrada['destino']}")
        print("-" * 50)
        print(f"STATUS ATUAL: {ordem_encontrada['status']}")
        print(f"PREVISÃO DE CHEGADA: {ordem_encontrada['previsao']}")
        print("\nHistórico de Status:")
        for tempo, status in ordem_encontrada['log_status']:
            print(f"  > {tempo} - {status}")
    else:
        print(f"❌ Rota '{rota_consulta}' não encontrada.")
    print("-" * 50)

def main():
    carregar_ordens()

    while True:
        print("\n--- Menu Principal da AgroRota ---")
        print("1. Registrar Nova Ordem de Entrega")
        print("2. Atualizar Status da Rota")
        print("3. Rastrear Ordem (Consultar Status)")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            registrar_nova_ordem()
        elif opcao == '2':
            atualizar_status()
        elif opcao == '3':
            rastrear_ordem()
        elif opcao == '4':
            print("Agradecemos por usar nosso sistema da AgroRota! 👋")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()