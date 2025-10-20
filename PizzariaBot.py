import os
from dotenv import load_dotenv 
# Carrega as variáveis de ambiente do arquivo .env
load_dotenv() 
import chainlit as cl
from groq import Groq

# --- Cardapio da Pizzaria ---
MENU = """
 *Pizzas:*
- Margarita ............ R$ 35
- Calabresa ............ R$ 38
- Quatro Queijos ....... R$ 42
- Frango com Catupiry .. R$ 40

 *Bebidas:*
- Refrigerante (lata) .. R$ 6
- Água .................. R$ 4
- Suco Natural .......... R$ 8
"""
# ----------------------------------

# Configuração do Cliente e Modelo Groq
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
# O cliente Groq é inicializado usando a chave API carregada do ambiente.
client = Groq(api_key=GROQ_API_KEY)
# Escolha do modelo
GROQ_MODEL = "llama-3.3-70b-versatile" 

@cl.on_chat_start
async def start():
    """É executado no início de cada sessão de chat."""
    
    # Configuração do System Prompt (Contexto para o LLM)
    system_message = (
        "Você é um assistente de atendimento ao cliente para uma pizzaria chamado 'PizzaBot'."
        "Sua função é responder perguntas sobre o cardápio, preços e receber pedidos. "
        "VOCÊ DEVE SEMPRE usar a seguinte informação do cardápio nas suas respostas. "
        "Se te perguntarem por algo que não está no cardápio, você deve dizer gentilmente que não o temos. "
        "--- CARDÁPIO DA PIZZARIA ---\n"
        f"{MENU}" 
        "\n---------------------------"
        "Você deve pedir o endereço no final do pedido."
        "Se o cliente finalizar o pedido, peça uma avaliação entre 1 e 5 estrelas pelo serviço."
        
    )
    
    # Iniciamos o historico de mensagems, considerando o contexto do sistema
    cl.user_session.set(
        "message_history",
        [
            {"role": "system", "content": system_message}
        ],
    )

    # Enviamos uma mensagem de bemvinda ao usuario
    await cl.Message(
        content="Olá! Sou PizzaBot, seu ssistente. Em que posso ajudar hoje? "
                "Se desejar, posso lhe mostrar nosso delicioso cardápio de pizzas e bebidas."
    ).send()


@cl.on_message
async def main(message: cl.Message):
    """Gerencia cada mensagem que o usuário envia."""
    
    # Recuperamos o histórico de mensagens da sessão do usuário.
    message_history = cl.user_session.get("message_history")
    # Adiciona a nova mensagem do usuário ao histórico.
    message_history.append({"role": "user", "content": message.content})
    # Inicia a mensagem de streaming na UI do Chainlit.
    msg = cl.Message(content="")
    await msg.send()

    try:
        # chamamos à API de Groq
        response_stream = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=message_history, # eviamos todo o historico
            temperature=0.5, 
            stream=True,
        )

        full_response = ""
        # Processamento e Streaming da resposta
        for chunk in response_stream:
            if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                await msg.stream_token(content)
                full_response += content
        # Finaliza a mensagem e salva a resposta do assistente no histórico.
        await msg.update()
        message_history.append({"role": "assistant", "content": full_response})

    except Exception as e:
        # Tratamento de Erros da API
        error_message = f"Ocurrió un error al contactar a Groq: {e}"
        await cl.Message(content=error_message).send()