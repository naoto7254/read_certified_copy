class TextProcessor:
    
    def __init__(self, text):
        self.text = text
    
    def clean_text(self):
        unnecessary_str = [' ', '\n', '\u3000', '━', '┯', '┼', '┓','┨', '─', '┬', '┷', '┴', '┏', '┛', '┗']
        
        for string in unnecessary_str:
            self.text = self.text.replace(string, '')
        
        return self.text
    
    def to_list(self, cleaned_text):
        text_list = cleaned_text.split('┃')
        return text_list
    
    def remove_value_from_array(self, array, value):
        while value in array:
            array.remove(value)