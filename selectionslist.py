class SelectionsList:
    def __init__(self):
        self.selections = []

    def add_selection(self, selection):
        self.selections.append(selection)
        print(f"Selection '{selection}' added to the list.")

    def get_selections(self):
        return self.selections

    def clear_selections(self):
        self.selections = []
