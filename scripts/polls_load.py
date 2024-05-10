import csv  # https://docs.python.org/3/library/csv.html

import datetime
from django.utils import timezone

from polls.models import Question, Choice

def run():
    print("=== Polls Loader")

    Choice.objects.all().delete()
    Question.objects.all().delete()
    print("=== Objects deleted")

    fhand = open('scripts/dj4e_batch.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    for row in reader:
        print(row)
        question_text = row[0]
        pub_date = timezone.now()
        q, created = Question.objects.get_or_create(question_text=question_text, pub_date=pub_date)
        for choice_text in row[1:]:
            if choice_text:  # Make sure there's something there
                # Create a Choice object for each non-empty choice string
                c = Choice(question=q, choice_text=choice_text,votes=0)
                # You could add default votes here if necessary, e.g., votes=0
                c.save()


        # Replace these comments to

        # Make a new Question and save it

        # Loop through the choice strings in row[1:] and add each choice,
        # connect it to the question and save it

        # Read and review the code for creating and saving Question objects
        # in Tutorial 2

    print("=== Load Complete")