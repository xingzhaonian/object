import os
with open('D:\\configs\\activity_main.txt', 'r', encoding = 'utf-8')as a,\
     open('D:\\configs\\activity_main1.txt', 'w', encoding = 'utf-8')as b:
    while True:
        old_txt_data = a.readline()
        print(old_txt_data[0:-2])
        b.write(old_txt_data[0:-2])
        b.write('\n')
        if not old_txt_data:
            break

os.remove('D:\\configs\\activity_main.txt')
os.rename('D:\\configs\\activity_main1.txt', 'D:\\configs\\activity_main.txt')


    
