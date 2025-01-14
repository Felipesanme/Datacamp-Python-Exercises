import spacy

nlp = spacy.load('en_core_web_sm')

DATA = [('One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin.',
  {'author': 'Franz Kafka', 'book': 'Metamorphosis'}),
 ("I know not all that may be coming, but be it what it will, I'll go to it laughing.",
  {'author': 'Herman Melville', 'book': 'Moby-Dick or, The Whale'}),
 ('It was the best of times, it was the worst of times.',
  {'author': 'Charles Dickens', 'book': 'A Tale of Two Cities'}),
 ('The only people for me are the mad ones, the ones who are mad to live, mad to talk, mad to be saved, desirous of everything at the same time, the ones who never yawn or say a commonplace thing, but burn, burn, burn like fabulous yellow roman candles exploding like spiders across the stars.',
  {'author': 'Jack Kerouac', 'book': 'On the Road'}),
 ('It was a bright cold day in April, and the clocks were striking thirteen.',
  {'author': 'George Orwell', 'book': '1984'}),
 ('Nowadays people know the price of everything and the value of nothing.',
  {'author': 'Oscar Wilde', 'book': 'The Picture Of Dorian Gray'})]

# Import the Doc class and register the extensions 'author' and 'book'
from spacy.tokens import Doc

Doc.set_extension('book', default=None)
Doc.set_extension('author', default=None)

for doc, context in nlp.pipe(DATA, as_tuples=True):
    # Set the doc._.book and doc._.author attributes from the context
    doc._.book = context['book']
    doc._.author = context['author']

    # Print the text and custom attribute data
    print(doc.text, '\n', "— '{}' by {}".format(doc._.book, doc._.author), '\n')