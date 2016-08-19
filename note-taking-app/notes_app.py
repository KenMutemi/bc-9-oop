class NotesApplication(object):


    def __init__(self, author, notes=[]):
        self.author = author
        self.notes = notes
    
    def create(self, note_content):
        self.notes.append(self.note_content)

    def list(self):
        pass

    def get(self, note_id):
        return note_id

    def search(self, search_text):

        return "Showing results for search " + search_text

    def delete(self, note_id):
        del notes[note_id]

    def edit(self, note_id, new_content):
        notes[note_id] = new_content

