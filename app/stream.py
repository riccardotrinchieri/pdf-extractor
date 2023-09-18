from app.preprocessing import break_into_sentences

def create_text_stream(text):
  sentences = break_into_sentences(text)
  for sentence in sentences:
    yield sentence
