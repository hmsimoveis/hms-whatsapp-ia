from flask import Flask, request, jsonify

app = Flask(__name__)

# Respostas automáticas baseadas em palavras-chave
responses = {
    "leilão": "Olá! Podemos te ajudar com informações sobre leilões. Qual sua dúvida específica?",
    "imóvel": "Está buscando um imóvel? Podemos te ajudar com leilões e oportunidades!",
    "investimento": "Investir em imóveis pode ser uma ótima escolha. Quer saber sobre rentabilidade?",
    "financiamento": "Podemos explicar as opções de financiamento em leilões. Quer mais detalhes?",
    "contato": "Se precisar de um atendimento humano, nos avise e encaminharemos seu contato.",
    "default": "Olá! Sou um assistente virtual da HMS Imóveis. Como posso te ajudar?"
}

@app.route('/whatsapp-ia', methods=['POST'])
def whatsapp_ia():
    data = request.form.to_dict()
    message = data.get("Body", "").lower()  # Captura a mensagem recebida

    # Verifica palavras-chave para responder de forma inteligente
    response_message = responses.get("default")
    for keyword in responses.keys():
        if keyword in message:
            response_message = responses[keyword]
            break

    return jsonify({"Body": response_message})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
