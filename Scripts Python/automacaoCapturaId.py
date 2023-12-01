import pandas as pd
import time
import pyautogui
import clipboard

favorec = []
idFavorecido = []
barra = 'id="favorecido"'

pyautogui.hotkey('alt','tab')

for i in range(0,len(favorec)):

    # clicar no no botão favorecido
    time.sleep(2)
    pyautogui.click(469,607)

    # clicar na guia favorecido

    time.sleep(1)
    pyautogui.click(685, 301)

    # colar cpf

    time.sleep(0.5)
    pyautogui.write(favorec[i])

    # esperar e clicar na lista suspensa

    time.sleep(3.5)
    pyautogui.click(689,331)

    # clicar no botão confirmar

    time.sleep(1)
    pyautogui.click(697,451)

    # clicar no botão atualizar

    time.sleep(1)
    pyautogui.click(1357,225)

    # a partir daqui será ctrl+u

    time.sleep(3)
    pyautogui.hotkey('ctrl','u')

    # ctrl+f

    time.sleep(1)
    pyautogui.hotkey('ctrl','f')

    # paste(id="favorecido"

    time.sleep(1)
    pyautogui.write(barra)

    # copiar trecho de id

    time.sleep(0.75)
    pyautogui.moveTo(161,585)
    pyautogui.mouseDown()
    pyautogui.moveTo(239,585)
    pyautogui.mouseUp()
    pyautogui.hotkey('ctrl','c')

    # salvar na lista

    termo = clipboard.paste()
    idFavorecido.append(termo)

    # ctrl+w
    time.sleep(0.5)
    pyautogui.hotkey('ctrl','w')

    # limpar filtro

    time.sleep(1.5)
    pyautogui.click(1470,93)

    time.sleep(1.5)
    pyautogui.click(1462, 78)

    time.sleep(1.5)
    pyautogui.hotkey('ctrl','home')
    print(termo, 'adicionado ao favorecido', favorec[i])

#########

print(idFavorecido)
# remover " da lista

caractere_para_remover = '"'

# Nova lista com o caractere removido
listaId = [item.replace(caractere_para_remover, '') for item in idFavorecido]

idList = pd.DataFrame(listaId)

idList.to_csv('id.csv', index= False)