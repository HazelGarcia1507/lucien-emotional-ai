#Codigo base
# ===== Repositorio emocional =====

emociones = {
    "tristeza": ["triste", "llorar", "apagado", "solo"],
    "enojo": ["enojado", "molesto", "furioso"],
    "miedo": ["miedo", "asustado", "nervios"],
    "alegria": ["feliz", "contento", "emocionado"]
}

# ===== Programa principal =====

while True:
    respuesta = input("Cuéntame, ¿qué pasó o cómo te sientes hoy? ").lower()

    if not respuesta.replace(" ", "").isalpha():
        print("Por favor, usa solo letras para que pueda entenderte mejor.\n")
        continue

    encontrado = False

    for emocion, palabras in emociones.items():
        for palabra in palabras:
            if palabra in respuesta:
                print(f"Parece que hay {emocion}.")
                encontrado = True
                break
        if encontrado:
            break

    if not encontrado:
        print("No logro identificar una emoción clara, y eso también está bien.")

    break
