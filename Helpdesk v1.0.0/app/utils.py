import spacy

def wczytaj_klucze_z_pliku(nazwa_pliku):
    with open(nazwa_pliku, 'r', encoding='utf-8') as file:
        zawartosc = file.read()
        klucze_slowa = [klucz.strip() for klucz in zawartosc.split('\n') if klucz.strip()]
    return klucze_slowa

def wyszukaj_slowa_kluczowe(zdanie, klucze_slowa):
    nlp = spacy.load("pl_core_news_sm")
    dokument = nlp(zdanie)

    slowa_kluczowe = [token.text for token in dokument if token.text.lower() in klucze_slowa]
    return slowa_kluczowe