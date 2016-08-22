def show_me_the_hand(records):
    lists = ['bawi', 'bawi', 'gawi', 'bo', 'bo', 'gawi', 'bo', 'bo', 'gawi', 'bo', 'bo', 'bawi', 'bo', 'gawi', 'gawi', 'bo', 'bawi', 'bo', 'gawi', 'gawi', 'gawi', 'bo', 'bawi', 'bo', 'gawi', 'bawi', 'bo', 'gawi', 'bo', 'bawi']
    return lists[len(records) % len(lists)-1]