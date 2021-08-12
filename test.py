test_list = [
    {
        'name': 'Joe',
        'age': 36,
        'height': 163
    },
    {
        'name': 'Bill',
        'age': 24,
        'height': 158
    },
    {
        'name': 'Jessie',
        'age': 66,
        'height': 170
    },
    {
        'name': 'Hector',
        'age': 21,
        'height': 167
    },
    {
        'name': 'Edgar',
        'age': 44,
        'height': 173
    }
]
print(sorted(test_list, key=lambda x: x['height']))






