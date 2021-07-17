# LED et GPIO

## Ecriture sur les LEDs

Pour facilité l'utilisation des LEDs, on utilise une liste d'objet ```struct led```, ainsi ```Leds[n] = {{LEDXX_GPIO_Port, LEDXX_Pin}}```.

On peut ainsi utilisé la ligne ```HAL_GPIO_WritePin(Leds[idx].port, Leds[idx].pin, !(charge-1<idx));``` ce qui simplifit l'itération sur toutes les leds.

## Lecture sur les boutons
On lis aussi l'état des bouton ```BP1``` et ```BP2``` via les GPIO.