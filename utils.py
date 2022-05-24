def get_clean_values(raw_values):
    return [value.strip() for value in raw_values.split('\n') if value.strip()]
