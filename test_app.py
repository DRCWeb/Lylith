import unittest
import json
from app import cargar_base_conocimientos, generar_respuesta, preprocesar_pregunta

class TestApp(unittest.TestCase):

    def setUp(self):
        self.base_conocimientos = {
            "¿cómo estás?": "Estoy bien, gracias.",
            "¿cuál es tu nombre?": "Soy un Lylith.",
            "¿qué haces?": "Estoy aquí para ayudarte.",
            "¿cuál es tu comida favorita?": "No como, soy un programa."
        }

    def test_cargar_base_conocimientos(self):
        base_conocimientos = cargar_base_conocimientos("knowledge.json")
        self.assertIsInstance(base_conocimientos, dict)
        self.assertIn("¿cómo estás?", base_conocimientos)
        self.assertEqual(base_conocimientos["¿cómo estás?"], "Estoy bien, gracias.")

    def test_generar_respuesta(self):
        respuesta = generar_respuesta("¿cómo estás?", self.base_conocimientos)
        self.assertEqual(respuesta, "Estoy bien, gracias.")
        respuesta = generar_respuesta("¿cuál es tu nombre?", self.base_conocimientos)
        self.assertEqual(respuesta, "Soy un Lylith.")
        respuesta = generar_respuesta("¿qué haces?", self.base_conocimientos)
        self.assertEqual(respuesta, "Estoy aquí para ayudarte.")
        respuesta = generar_respuesta("¿cuál es tu comida favorita?", self.base_conocimientos)
        self.assertEqual(respuesta, "No como, soy un programa.")
        respuesta = generar_respuesta("¿cuál es tu color favorito?", self.base_conocimientos)
        self.assertEqual(respuesta, "Lo siento, no puedo responder esa pregunta.")

    def test_preprocesar_pregunta(self):
        pregunta = "¿Cómo estás?"
        pregunta_procesada = preprocesar_pregunta(pregunta)
        self.assertEqual(pregunta_procesada, "¿cómo estar?")

    def test_chatbot_functionality(self):
        pregunta = "¿Cómo estás?"
        respuesta = generar_respuesta(pregunta, self.base_conocimientos)
        self.assertEqual(respuesta, "Estoy bien, gracias.")
        pregunta = "¿Cuál es tu nombre?"
        respuesta = generar_respuesta(pregunta, self.base_conocimientos)
        self.assertEqual(respuesta, "Soy un Lylith.")
        pregunta = "¿Qué haces?"
        respuesta = generar_respuesta(pregunta, self.base_conocimientos)
        self.assertEqual(respuesta, "Estoy aquí para ayudarte.")
        pregunta = "¿Cuál es tu comida favorita?"
        respuesta = generar_respuesta(pregunta, self.base_conocimientos)
        self.assertEqual(respuesta, "No como, soy un programa.")
        pregunta = "¿Cuál es tu color favorito?"
        respuesta = generar_respuesta(pregunta, self.base_conocimientos)
        self.assertEqual(respuesta, "Lo siento, no puedo responder esa pregunta.")

if __name__ == '__main__':
    unittest.main()
