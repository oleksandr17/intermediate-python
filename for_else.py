list = [1, 2, 3, 4, 5]
target_item = 5
for item in list:
    if item == target_item:
        print('Target item found: {}'.format(target_item))
        break
else:
    print('Target item not found: {}'.format(target_item))
