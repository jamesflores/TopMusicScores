from elasticsearch_dsl import Document, Text, Float

class SheetMusicIndex(Document):
    rank = Float()
    item_url = Text()
    cover_url = Text()
    title = Text()
    title_slug = Text()
    artist = Text()
    instruments = Text()
    format = Text()
    genres = Text()
    lead_time = Text()
    list_price = Float()
    publisher = Text()
    isbn = Text()
    item_type = Text()
    description = Text()

    class Index:
        name = 'sheet_music'