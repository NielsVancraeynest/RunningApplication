import flet as ft
import time 

trainingDict = {"Dag1": {"Type": ["Wandelen", "Lopen", "X", "Wandelen"],"Tijden":[5,7,1,15]},
                "Dag2": {"Type": ["Wandelen", "Lopen", "Wandelen"],"Tijden":[1,2,5]}}



def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    audio1 = ft.Audio(
                src="https://luan.xyz/files/audio/ambient_c_motion.mp3",
            )
    page.overlay.append(audio1)


    def countdown(tijd, timerPage:ft.Text):
        t = tijd #To count down with seconds
        while t: 
            mins, secs = divmod(t, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs) 
            timerPage.value=timer
            page.update()
            print(timer, end="\r") 
            time.sleep(1) 
            t -= 1
            if tijd-2 ==t:
                print("audio paused")
                audio1.pause()
            elif t==2:
                audio1.play()
    def changeTraining(e):
        page.clean()
        timerText = ft.Text("00:00", weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.HEADLINE_LARGE)
        typeText = ft.Text("Lopen",weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.HEADLINE_LARGE)
        page.add(timerText)
        page.add(typeText)

        indexPreviosRep = 0
        for i,tijd in enumerate(trainingDict[selectTraining.value]["Tijden"]):
            if trainingDict[selectTraining.value]["Type"][i] == "X":
                repetitie = tijd
                for j in range(repetitie-1):
                    for k in range(i-indexPreviosRep):
                        typeText.value = trainingDict[selectTraining.value]["Type"][k]
                        page.update()
                        countdown(trainingDict[selectTraining.value]["Tijden"][k], timerText)
                indexPreviosRep = i
            else:
                typeText.value = trainingDict[selectTraining.value]["Type"][i]
                page.update()
                countdown(tijd, timerText)
            
        print("Training is afgelopen")
        return
    selectTraining = ft.Dropdown(label='Selecteer activiteit',
                        options=[ft.dropdown.Option(training) for training in trainingDict],
                        on_change= changeTraining)
    page.add(selectTraining)
    
    return
ft.app(target=main)
