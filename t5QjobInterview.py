from transformers import pipeline

# Charger le pipeline pour la génération de texte en utilisant FLAN-T5 large
generator = pipeline("text2text-generation", model="google/flan-t5-large")

def generate_questions(text, num_questions=10):
    # Préparer l'entrée pour le pipeline
    prompt = f"Generate {num_questions} interview questions based on the following text:\n\n{text}"
    
    # Générer des questions
    response = generator(prompt, max_length=150, num_return_sequences=num_questions)
    
    # Extraire les questions générées
    questions = [res['generated_text'] for res in response]
    return questions

# Exemple de texte donné
text = """L'intelligence artificielle (IA) est un domaine vaste de l'informatique qui se concentre sur la création de systèmes capables d'accomplir des tâches nécessitant normalement l'intelligence humaine. Cela inclut des domaines comme la reconnaissance vocale, la vision par ordinateur, la compréhension du langage naturel, la planification, et la prise de décision. Les algorithmes d'apprentissage automatique sont une sous-catégorie de l'IA qui apprend à partir de données. Ils jouent un rôle clé dans le développement des technologies d'IA modernes."""

# Générer des questions
questions = generate_questions(text, num_questions=10)

# Afficher les questions générées
for idx, question in enumerate(questions, 1):
    print(f"Q{idx}: {question}")
