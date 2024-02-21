from flask import Flask, render_template, request
import openai 

openai.api_key = "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"

# Contexto del asistente
context = {"role":"system","context":"Eres un asistente muy útil"}
messages = [context]

def chatgpt_response(msg):
    messages.append({"role":"user","context":msg}) # agregar nuevo elemento al array de arriba, msg - mesaje del usuario
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages) # subclase para construir mensages, modelo de la red neural a utilizar
    response_content = response.choises[0].message.content # primer elemento del listado, esta variable guarda la respuesta en string de caht gpt
    messages.append({"role":"assistant", "content":response_content})
    
    return response_content # regresa la respuesta en string de chat gpt

app = Flask(__name__) # se crea un objeto de la clase Flask
app.static_folder = 'static'  # el folder 'estático' es donde se dibuja el estilo para la interfás de la App

@app.route("/") # vista base
def home():
    return render_template("index.html")

@app.route("/get") # cuando se evoque un get, se regresa algo ... 
def get_bot_response(): # la respuesta de chat gpt
    userText = request.args.get('msg') # argumentos del request son el mensage del usuario y lo guarda en la variable
    return chatgpt_response(userText)

print("Hello World")
if __name__ == "__main__":
    app.run()
    

# lógica de backend del bot que utiliza chatgpt
    