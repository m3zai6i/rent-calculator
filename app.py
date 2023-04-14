import PySimpleGUI as sg

# define the layout of the GUI
layout = [
    [sg.Text("RENT"), sg.InputText()],
    [sg.Text("BILL"), sg.InputText()],
    [sg.Text("NET"), sg.InputText()],
    [sg.Button("Calculate")],
    [sg.Text("", size=(60, 10), key="-OUTPUT-")],
]

# create the window
window = sg.Window("Rent (FAIR) Distribution", layout)

# start the event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Calculate":
        # get the input values
        rent = float(values[0])
        bill = float(values[1])
        net = float(values[2])
        no_of_persons = 6

        # Rent calculation as per FAIR DISTRIBUTION

        Rent = round(rent/3,1)
        Bill = round(bill/no_of_persons,1)
        Net = round(net/no_of_persons,1)

        room_1 = round((Rent+500)/1,1)
        room_2 = round((Rent+500)/2,1)
        room_3 = round((Rent-1000)/3,1)

        person1_share = room_1+Bill+Net #Shahzaib
        person2_share = room_2+Bill+Net #Asad
        person3_share = room_2+Bill+Net #Qadeer
        person4_share = room_3+Bill+Net #Arsalan
        person5_share = room_3+Bill+Net #Umer
        person6_share = room_3+Bill+Net #Mehbub

        total_rent = person1_share+person2_share+person3_share+person4_share+person5_share+person6_share

        print('------ FAIR DISTRIBUTION ------')
        print('RENT DIVIDED ON 3 ROOMS')
        print('RESOURCES DIVIDED ON NUMBER OF PERSONS LIVING')
        print('')
        print('RENT = '+str(rent)+'/'+str(3)+' =',Rent)
        print('BILL = '+str(bill)+'/'+str(no_of_persons)+' =',Bill)
        print('NET = '+str(net)+'/'+str(no_of_persons)+' =',Net)
        print('')
        print('ROOM 1 = ('+str(round(rent/3,1))+'+500)/(1) = '+str(room_1)+' (PER HEAD)')
        print('ROOM 2 = ('+str(round(rent/3,1))+'+500)/(1+1) = '+str(room_2)+' (PER HEAD)')
        print('ROOM 3 = ('+str(round(rent/3,1))+'-1000)/(1+1+1) = '+str(room_3)+' (PER HEAD)')
        print('')
        print('ARSALAN = '+str(room_3)+'+'+str(Bill)+'+'+str(Net)+' = '+str(person6_share))
        print('UMER = '+str(room_3)+'+'+str(Bill)+'+'+str(Net)+' = '+str(person5_share))
        print('MAHBUB = '+str(room_3)+'+'+str(Bill)+'+'+str(Net)+' = '+str(person4_share))
        print('')
        print('ASAD = '+str(room_2)+'+'+str(Bill)+'+'+str(Net)+' = '+str(person3_share))
        print('QADEER = '+str(room_2)+'+'+str(Bill)+'+'+str(Net)+' = '+str(person2_share))
        print('')
        print('SHAHZAIB = '+str(room_1)+'+'+str(Bill)+'+'+str(Net)+' = '+str(person1_share))
        print('')
        print('TOTAL =',round(total_rent,1))

        # update the output label
        output_text = f"Shahzaib: {person1_share:.2f}\nAsad: {person2_share:.2f}\nQadeer: {person3_share:.2f}\nArsalan: {person4_share:.2f}\nUmer: {person5_share:.2f}\nMehbub: {person6_share:.2f}\n\nTotal: {total_rent:.2f}"
        window["-OUTPUT-"].update(output_text)

# close the window
window.close()


'''
---------------------------------

BILL Discription:

- 700 water bill (Divided equally)
- 3000 maintenance (lift + outdoor cleaniness + flat) (Divided equally)
- remaining is electricity bill (most usage Fridge, Gyser) (Divided Equally)
- Room1 < (Room2 & HallRoom) Electricity usage is less then other rooms.

----------------------------------

'''
