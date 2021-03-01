remind = input('Do you have any reminders to set: ')

if (remind == 'yes'):
    response1 = input('Type a reminder here: ')
    remind = input('Do you have any more reminders: ')
    if(remind == 'yes'):
        response2 = input('Type another reminder here: ')
        print('Reminders:' + ' ' + response1 + ',and' + ' ' + response2)
    else:
        print('reminders:' + ' ' + response1)
elif (remind == 'no'):
    print('Ok! Come back and type a reminder another time')
else:
    print('Type Yes or No only')