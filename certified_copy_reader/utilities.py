def to_lower_number(string):
    translation_table = str.maketrans('０１２３４５６７８９', '0123456789')
    result = string.translate(translation_table)
    
    return result

def convert_to_float(string):
    parts = [part.strip() for part in string.replace('：', '.').split('.') if part.strip()]
    result = float('.'.join(parts[:2])) if parts else None
    
    return result