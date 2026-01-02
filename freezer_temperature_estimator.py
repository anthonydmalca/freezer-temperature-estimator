
off = True #If off, execute the outermost while loop

while off:


    while True: #check to see if fridge is powered 

        try:

            query = input("Does your fridge have power? (Y/N): ")

            if query.lower() != "y" and query.lower() != "n": #catching invalid inputs with an AND to indicate the inputs we want

                raise ValueError ("Please enter (Y/N)")
            
            if query.lower() == "y": 

                print("Ok, great!")
                off = False 
                break  #Since fridge is powered, we must terminate program execution by exiting ALL the while loops;
                        #To do this, we must first break out of the first while loop 

            else: #if fridge isn't powered, we still need to break out of the current while loop, but the remainder of the code executes inside the outermost loop

                break

        except ValueError as c: #Printing the error 
            
            print("Invalid Input:", c ) 

    if off == False: #We catch that (off == False) and skip the remainder of the code; crucially, this breaks out of the outermost loop by tripping its condition

        continue 

    else: #otherwise, execute the rest of it, because off is True 


        isroomTemp = False #track whether fridge temperature has reached roomTemp
        
        while True:

            try:

                inputStr = input("How long has it been since the power failure? (HH:MM): ") #repeatedly prompt the user with the question until valid input is received 
                print()
 
                hrsMins = inputStr.split(':') #creates a list of substrings of inputStr split at ':'

                if len(hrsMins) !=2: #by definition, there should only be 2 elements in hrsMins ['HH', 'MM']; if user entered HHMM, there's no ':'
                    
                    raise ValueError("Missing ':' separator")

                hrs = int(hrsMins[0]) #get hrs
                mins = int(hrsMins[1]) #get mins

                #---------------------------------------------------------------------------------
                #---------------------------------------------------------------------------------

                hours = hrs + (mins/60) #calculate total hours elapsed

                if hours > 11.99: #room temperature is achieved in around 12hrs after outage

                    isroomTemp = True 

                if mins < 0 or mins > 59:

                    raise ValueError("Minutes must be between 0 and 59") #more input handling 
                
                break


            except ValueError as e:

                if str(e):
                    
                    print("Invalid input:", e)

                else:

                    print("Please enter integers in the form of HH:MM.")


#---------------------------------------------------------------------------------
        # Calculating Variables and Conversions
#---------------------------------------------------------------------------------


        roomTemp = 21.1 #around 70 degrees fahrenheit
        roomTempInFaren = 70 #conversion

        
        freezerTemp = ((4*(hours)**2)/(hours + 2)) - 20 #freezerTemp as a function of time
        freezerTempinFaren = ((9/5)*freezerTemp) + 32 #conversion of freezer temperature to fahrenheit
        
        

#---------------------------------------------------------------------------------
        # Displaying Freezer Temperature
#---------------------------------------------------------------------------------


        print(f"Freezer temperature {hours:.2f} hours after power failure: {f"{freezerTemp:.1f}C ({freezerTempinFaren:.1f} degrees F)" if not isroomTemp else f"{roomTemp}C ({roomTempInFaren} degrees F)"}")


#---------------------------------------------------------------------------------
        # Ice Cream Melt Detection
#---------------------------------------------------------------------------------

        if freezerTemp > -10:

            print("If you have ice-cream in the freezer, it is now melting") if (abs(freezerTemp + 10) < 1) else print("If you have ice-cream in the freezer, it has already melted")
            
#---------------------------------------------------------------------------------
        # Spoilage Detection
#---------------------------------------------------------------------------------

        if freezerTemp > 4.5:

            print("If you have meat/poultry products in the freezer, it's time to discard them")

                        
        
        
