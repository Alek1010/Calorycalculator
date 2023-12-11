def main():
    activity = [1, 1.12, 1.24, 1.48]
    thermic_effect = int(input('enter thermic effect'))

    def client_weight():
        BW = input('enter the clients body weight: ')
        try:
            float(BW)
            return float(BW)


        except ValueError:
            print('enter a valid number value')
            main()

    def client_body_fat():
        BF = input('enter the clients body fat percentage')
        try:
            float(BF)
            return float(BF)

        except ValueError:
            print('enter a valid value')
            client_body_fat()

    def client_activity():
        act = float(input('enter activity level of\n1\n1.24\n1.12\n1.48\n'))
        try:

            if act in activity:
                print(act)
                return act



            else:
                print('enter valid num')
                client_activity()

        except ValueError:
            print('enter a valid value')
            client_activity()

    def BMRcalculation(BW, BF,):
        Fat = float(BW) * float(BF) / 100
        FFM = float(BW) - float(Fat)
        BMR = 370 + 21.6 * FFM
        return FFM, BMR

    def Activity_calculations(BMR,act):
        thermic = BMR*thermic_effect/100
        maintance = (BMR + thermic)*act
        return maintance

    def defecit_surplus(maintance):
        choice = input('enter D if you want deficit. \n '
                       'or enter S if you want surplus \n').upper()
        if choice == 'D':
            d_amount = float(input('enter the defacit %'))
            cal = (maintance*d_amount)/100
            defacit = maintance-cal

            return defacit
        elif choice =='S':
            S_amount = float(input('enter the surplus percentage %'))
            cal_2 = (maintance* S_amount)/100
            surplus =  maintance + cal_2

            return surplus

    def protien(BW,FFM):
        protien_calc = input('how would you like to calculate your protien FFM or BW').upper()
        if protien_calc == 'FFM':
            protein_in_G = FFM * 2.25
            Protein_In_cal = protein_in_G * 4


        elif protien_calc == 'BW':
            protein_in_G = BW * 1.8
            Protein_In_cal = protein_in_G *4

        return protein_in_G, Protein_In_cal


    def macros(protein_cal,final_defacit):
        FAT_calc = input('percentage of fat in diet')
        try:
            int(FAT_calc)
        except ValueError:
            print('enter an int')
            while ValueError:
                FAT_calc = input('percentage of fat in diet')
        Fat_CAL = (int(final_defacit) *int(FAT_calc))/100


        FAT_in_G = Fat_CAL/9

        Carb_in_cal = final_defacit-(Fat_CAL+protein_cal)
        Carb_in_g = Carb_in_cal/4


        return Fat_CAL,Carb_in_cal,FAT_in_G,Carb_in_g


    def display(final_deficit,maintance,BMR,act,BF,BW,protein_cal, fat_cal, carbs_cal,protein_g,fat_g,carb_g):
        print('total calories are,',int(final_deficit),'\n'
                'your maintance is,', int(maintance),'\n'
                'your BMR is,',BMR,'\n'
                'your activity level is,',act,'\n'
                'your body fat is,',BF,'%\n'
                'your body weight is,',BW,)

        print('\n')
        print('protein',int(protein_g),int(protein_cal),'\n'
              'fat',int(fat_g),int(fat_cal),'\n'
              'carns',int(carb_g),int(carbs_cal))






    BW = client_weight()
    BF = client_body_fat()
    act = client_activity()
    FFM,BMR = BMRcalculation(BW, BF, )
    maintance = Activity_calculations(BMR,act)
    final_deficit = defecit_surplus(maintance)
    protein_g, protein_cal = protien(BW,FFM)
    fat_cal, carbs_cal,fat_g,carb_g = macros(protein_cal,final_deficit)
    display(final_deficit, maintance, BMR, act, BF, BW,protein_cal, fat_cal, carbs_cal,protein_g,fat_g,carb_g)

main()