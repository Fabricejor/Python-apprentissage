from transformers import pipeline

# Charger le pipeline de génération de questions
question_generator = pipeline("text2text-generation", model="valhalla/t5-small-qg-prepend")

texte = "Python est un langage de programmation interprété, de haut niveau et à la syntaxe claire."
task_prefix ="generate question"
questions = question_generator(task_prefix + texte)

# Afficher les questions générées
for question in questions:
    print(question["question"])
