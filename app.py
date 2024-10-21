import random
import json
import spacy

def cargar_base_conocimientos(archivo):
    with open(archivo, 'r') as f:
        base_conocimientos = json.load(f)
    return base_conocimientos

nlp = spacy.load("es_core_news_sm")

def preprocesar_pregunta(pregunta):
    doc = nlp(pregunta)
    tokens = [token.lemma_.lower() for token in doc]
    return " ".join(tokens)

def generar_respuesta(pregunta, base_conocimientos):
    pregunta = preprocesar_pregunta(pregunta)
    respuesta = base_conocimientos.get(pregunta, "Lo siento, no puedo responder esa pregunta.")
    return respuesta

# Cargar la base de conocimientos desde el archivo JSON
base_conocimientos = cargar_base_conocimientos("knowledge.json")

# Ejemplo de uso
while True:
    pregunta_usuario = input("Escribe tu pregunta: ")
    if pregunta_usuario.lower() == 'salir':
        break
    print(f"Respuesta del chatbot: {generar_respuesta(pregunta_usuario, base_conocimientos)}")
