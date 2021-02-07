with open('class_roll.txt') as f1, open('students_webwork.lst', 'w') as f2:
    for line in f1:
        parts = line.split(',')
        num_id = parts[0]
        last = parts[1]
        first = parts[2]
        email = parts[-1][0:-1]
        user_id = email.split('@')[0]
        
        print('{},{},{},c,,,,{},{},,'.format(num_id, \
               last, first, email, user_id), file = f2)
