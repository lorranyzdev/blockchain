from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Blockchain da Lorrany</h1>
        <form action="/mine_block" method="post" onsubmit="event.preventDefault(); enviarMensagem();">
            <input type="text" id="mensagem" placeholder="Escreva sua mensagem">
            <button type="submit">Minerar bloco com mensagem</button>
        </form>
        <br>
        <a href="/chain" target="_blank">Ver Blockchain</a>

        <script>
        function enviarMensagem() {
            const mensagem = document.getElementById("mensagem").value;
            fetch("/mine_block", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: mensagem })
            })
            .then(response => response.json())
            .then(data => alert("✅ Bloco minerado!\\n" + JSON.stringify(data.block, null, 2)))
            .catch(error => alert("Erro ao minerar: " + error));
        }
        </script>
    '''
