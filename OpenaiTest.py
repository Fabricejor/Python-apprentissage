import openai

# Insère ta clé API ici

# Effectuer une requête de complétion
completion = openai.ChatCompletion.create(
    model="gpt-4o-mini",  # Assure-toi que le modèle existe et remplace "gpt-4o-mini" par "gpt-4" ou autre si nécessaire
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a speech to introduce yourself."}
    ]
)

# Afficher le message de la première réponse
print(completion.choices[0].message["content"])
