import openai

# Insère ta clé API ici
openai.api_key = "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"

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
