from random import randint

def get_random_summary():
    summaries = [
        #add about your self
        '''summary 1''',
        '''summary 2''',
        '''summary 3''',
        '''summary 4''',
        '''summary 5''',
    ]

    return summaries[randint(0, (len(summaries)-1))]