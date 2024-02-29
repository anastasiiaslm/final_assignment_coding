df = pd.read_csv('https://github.com/MarcKaufmann/R-Coding/blob/master/data-reports/data-report2/opinions.csv')

# Using Python “lists” and “dictionaries” 

selected_questions = ['heard-of-last-week', 'how-often-talk-colleagues', 'how-often-talk-family']

answer_frequencies = {}

for question in selected_questions:
    answer_frequencies[question] = df[question].value_counts()
  print(df[question].value_counts())