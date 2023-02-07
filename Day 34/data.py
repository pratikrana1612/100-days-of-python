import requests

parameters={
    'amount':10,
    'type':'boolean'
}

response=requests.get('https://opentdb.com/api.php',params=parameters)
response.raise_for_status()
data=response.json()
# print(data['results'])

question_data = data['results']



#   "response_code": 0,
#   "results": [
#     {
#       "category": "Entertainment: Video Games",
#       "type": "boolean",
#       "difficulty": "easy",
#       "question": "In &quot;Sonic Adventure&quot;, you are able to transform into Super Sonic at will after completing the main story.",
#       "correct_answer": "False",
#       "incorrect_answers": [
#         "True"
#       ]
#     },
#     {
#       "category": "Entertainment: Video Games",
#       "type": "boolean",
#       "difficulty": "medium",
#       "question": "TF2: The Medic will be credited for an assist if he heals a Spy that successfully saps a building.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "category": "Science: Computers",
#       "type": "boolean",
#       "difficulty": "easy",
#       "question": "In most programming languages, the operator ++ is equivalent to the statement &quot;+= 1&quot;.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "category": "Politics",
#       "type": "boolean",
#       "difficulty": "medium",
#       "question": "During the 2016 United States presidential election, the State of California possessed the most electoral votes, having 55.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "category": "History",
#       "type": "boolean",
#       "difficulty": "medium",
#       "question": "Martin Luther King Jr. and Anne Frank were born the same year. ",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "category": "Entertainment: Video Games",
#       "type": "boolean",
#       "difficulty": "medium",
#       "question": "In Riot Games &quot;League of Legends&quot; the name of Halloween event is called &quot;The Reckoning&quot;.",
#       "correct_answer": "False",
#       "incorrect_answers": [
#         "True"
#       ]
#     },
#     {
#       "category": "History",
#       "type": "boolean",
#       "difficulty": "hard",
#       "question": "During the Winter War, the amount of Soviet Union soliders that died or went missing was five times more than Finland&#039;s.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "category": "Entertainment: Japanese Anime & Manga",
#       "type": "boolean",
#       "difficulty": "hard",
#       "question": "In the &quot;Kagerou Daze&quot; series, Shintaro Kisaragi is prominently shown with the color red.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "category": "History",
#       "type": "boolean",
#       "difficulty": "easy",
#       "question": "The United States of America was the first country to launch a man into space.",
#       "correct_answer": "False",
#       "incorrect_answers": [
#         "True"
#       ]
#     },
#     {
#       "category": "Vehicles",
#       "type": "boolean",
#       "difficulty": "medium",
#       "question": "The snowmobile was invented by Canadian Joseph-Armand Bombardier in 1937.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     }
#   ]
# }