from time import sleep
import emoji
for c in range(10, -1, -1):
    print('\033[1;33m', c)
    sleep(1)
print(emoji.emojize(':colisão::colisão::colisão::colisão:', language='pt'))
print(emoji.emojize(':colisão:BUUM:colisão:', language='pt'))
print(emoji.emojize(':colisão::colisão::colisão::colisão:', language='pt'))