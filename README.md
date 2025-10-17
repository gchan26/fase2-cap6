# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# AgroRota - Sistema de Rastreamento de Entregas

## 👨‍🎓 Integrantes:
- Jacqueline Nanami - RM568498  
- Davis Roberto - RM567941  
- Guilherme Chan - RM567722  

## 📜 Descrição

O **AgroRota** é um sistema de rastreamento de ordens de entrega desenvolvido em **Python**, com foco em gerenciamento logístico e controle de rotas no setor agroindustrial.  
O programa permite registrar novas ordens de entrega, atualizar o status de cada rota e rastrear o progresso em tempo real, armazenando os dados localmente em arquivos JSON e logs em texto.

O sistema foi projetado para ser simples, leve e executável diretamente em ambientes locais, sem dependência de banco de dados externos. Seu objetivo é oferecer uma simulação funcional de um painel de controle de entregas, útil para o aprendizado de conceitos de **persistência de dados**, **tratamento de erros**, **estruturação modular de código** e **interface de linha de comando interativa**.

### Funcionalidades principais:
- Registro de novas ordens de entrega com ID da rota, destino e previsão de chegada.  
- Atualização de status (ex: EM TRÂNSITO, ATRASADA, ENTREGUE).  
- Cálculo automático da previsão de chegada com base no tempo estimado.  
- Histórico de status com data e hora de cada atualização.  
- Log de eventos registrado em arquivo `.txt` para auditoria.  

Este projeto faz parte do desenvolvimento prático das disciplinas de **Lógica de Programação e Algoritmos** e **Fundamentos de Computação**, integrando conceitos fundamentais de entrada/saída de dados, manipulação de arquivos e estruturação modular de código.

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- **assets**: arquivos visuais como o logotipo da FIAP.  
- **src**: contém o código-fonte principal do sistema (`Cap6Fase2.py` e módulos auxiliares).  
- **README.md**: guia explicativo geral sobre o projeto.  
- **ordens_entrega.json**: arquivo gerado automaticamente para armazenamento das ordens registradas.  
- **log_rastreamento.txt**: arquivo de log contendo o histórico de eventos do sistema.  

## 🔧 Como executar o código

### Pré-requisitos
- **Python 3.8+** instalado na máquina.  
- Nenhuma biblioteca externa é necessária além das nativas do Python.

### Passo a passo

1. **Baixar o código**
   ```bash
   git clone https://github.com/gchan26/fase2-cap6.git
   cd fase2-cap6
   ```

2. **Executar o script principal**
   ```bash
   python src/Cap6Fase2.py
   ```

3. **Navegar pelo menu**
   - Opção 1: Registrar nova ordem de entrega  
   - Opção 2: Atualizar status da rota  
   - Opção 3: Rastrear ordem  
   - Opção 4: Sair  

O programa criará automaticamente os arquivos `ordens_entrega.json` e `log_rastreamento.txt` na pasta raiz para armazenar as informações.

## 🗃 Histórico de lançamentos

* 1.0.0 - 17/10/2025  
    * Lançamento inicial do sistema AgroRota  
    * Funções de cadastro, atualização e rastreamento concluídas  
    * Estrutura modular e logs implementados  

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
