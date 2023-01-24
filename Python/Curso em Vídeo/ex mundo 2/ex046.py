from time import sleep
import emoji
em = emoji.emojize(':collision:', use_aliases=True)

for c in range(10, -1, -1):
    sleep(1)
    print(c)
sleep(1)
print('{}FOGOS{}'.format(em, em))


