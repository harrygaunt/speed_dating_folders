import os
import shutil
import time
from datetime import datetime
#imports the librarys I need 
#--------------------------------------------------------------------------------
a=(input(print("""

 ____  ____  ____  ____  ____    ____  __ _  ____  ____  ____ 
(  _ \(  _ \(  __)/ ___)/ ___)  (  __)(  ( \(_  _)(  __)(  _ \       
 ) __/ )   / ) _) \___ \\___ \   ) _) /    /  )(   ) _)  )   /       
(__)  (__\_)(____)(____/(____/  (____)\_)__) (__) (____)(__\_)       
 ____  __      ___  __   __ _  ____  __  __ _  _  _  ____    _       
(_  _)/  \    / __)/  \ (  ( \(_  _)(  )(  ( \/ )( \(  __)  (_)      
  )( (  O )  ( (__(  O )/    /  )(   )( /    /) \/ ( ) _)    _       
 (__) \__/    \___)\__/ \_)__) (__) (__)\_)__)\____/(____)  (_)   



\n""")))
path = os.getcwd()
#gets current directory location

print ("The current working directory is %s" % path)
#prints current directory location



for file in os.listdir(path):
#runs through every item in the current directory location
    if file != ("speed_dating_folders.py"):
    # prevents script from moving itself to a folder
        
        print("\n",file)
        #prints the name of the current item
        
        alfa=(os.path.getmtime(file))
        #gets the modification date of the current file as a weird format
        #change "getmtime" to "getctime" for the creation date (fairly buggy)
        
        dir_name=(datetime.fromtimestamp(alfa).strftime('%d%m%y'))
        #turns the creation date into 'ddmmyy' with nothing seperating them
              
        print("\nLast modified: %s" % datetime.fromtimestamp(alfa).strftime('%d:%m:%Y'))
        #prints the creation date of the current file

        dir_path = path + ("\\") + dir_name
        print("\n"f'dir_path: {dir_path}')
        
        # check if directory exists or not yet
        if not os.path.exists(dir_path):
        # check if directory exists
            os.makedirs(dir_path)
            

        if os.path.exists(dir_path):
            file_path = path + ("\\") + file
            
            
            shutil.move(file_path, dir_path)
            # move files into specified directory
            
        print("\n\n","file:  \'",file," \' complete! \n \n \n")
        #prints file: "file_name" complete
        
        print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
        #hmmm, I wonder what this line does
        
        time.sleep(0.075)
        #waits 0.25 of a seccond so people can admire the output/ui (should probably get deleted)

print("""
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
                CCCCCCCCCCCCC          OOOOOOOOO          MMMMMMMM               MMMMMMMM     PPPPPPPPPPPPPPPPP        LLLLLLLLLLL                  EEEEEEEEEEEEEEEEEEEEEE     TTTTTTTTTTTTTTTTTTTTTTT     EEEEEEEEEEEEEEEEEEEEEE
             CCC::::::::::::C        OO:::::::::OO        M:::::::M             M:::::::M     P::::::::::::::::P       L:::::::::L                  E::::::::::::::::::::E     T:::::::::::::::::::::T     E::::::::::::::::::::E
           CC:::::::::::::::C      OO:::::::::::::OO      M::::::::M           M::::::::M     P::::::PPPPPP:::::P      L:::::::::L                  E::::::::::::::::::::E     T:::::::::::::::::::::T     E::::::::::::::::::::E
          C:::::CCCCCCCC::::C     O:::::::OOO:::::::O     M:::::::::M         M:::::::::M     PP:::::P     P:::::P     LL:::::::LL                  EE::::::EEEEEEEEE::::E     T:::::TT:::::::TT:::::T     EE::::::EEEEEEEEE::::E
         C:::::C       CCCCCC     O::::::O   O::::::O     M::::::::::M       M::::::::::M       P::::P     P:::::P       L:::::L                      E:::::E       EEEEEE     TTTTTT  T:::::T  TTTTTT       E:::::E       EEEEEE
        C:::::C                   O:::::O     O:::::O     M:::::::::::M     M:::::::::::M       P::::P     P:::::P       L:::::L                      E:::::E                          T:::::T               E:::::E             
        C:::::C                   O:::::O     O:::::O     M:::::::M::::M   M::::M:::::::M       P::::PPPPPP:::::P        L:::::L                      E::::::EEEEEEEEEE                T:::::T               E::::::EEEEEEEEEE   
        C:::::C                   O:::::O     O:::::O     M::::::M M::::M M::::M M::::::M       P:::::::::::::PP         L:::::L                      E:::::::::::::::E                T:::::T               E:::::::::::::::E   
        C:::::C                   O:::::O     O:::::O     M::::::M  M::::M::::M  M::::::M       P::::PPPPPPPPP           L:::::L                      E:::::::::::::::E                T:::::T               E:::::::::::::::E   
        C:::::C                   O:::::O     O:::::O     M::::::M   M:::::::M   M::::::M       P::::P                   L:::::L                      E::::::EEEEEEEEEE                T:::::T               E::::::EEEEEEEEEE   
        C:::::C                   O:::::O     O:::::O     M::::::M    M:::::M    M::::::M       P::::P                   L:::::L                      E:::::E                          T:::::T               E:::::E             
         C:::::C       CCCCCC     O::::::O   O::::::O     M::::::M     MMMMM     M::::::M       P::::P                   L:::::L         LLLLLL       E:::::E       EEEEEE             T:::::T               E:::::E       EEEEEE
          C:::::CCCCCCCC::::C     O:::::::OOO:::::::O     M::::::M               M::::::M     PP::::::PP               LL:::::::LLLLLLLLL:::::L     EE::::::EEEEEEEE:::::E           TT:::::::TT           EE::::::EEEEEEEE:::::E
           CC:::::::::::::::C      OO:::::::::::::OO      M::::::M               M::::::M     P::::::::P               L::::::::::::::::::::::L     E::::::::::::::::::::E           T:::::::::T           E::::::::::::::::::::E
             CCC::::::::::::C        OO:::::::::OO        M::::::M               M::::::M     P::::::::P               L::::::::::::::::::::::L     E::::::::::::::::::::E           T:::::::::T           E::::::::::::::::::::E
                CCCCCCCCCCCCC          OOOOOOOOO          MMMMMMMM               MMMMMMMM     PPPPPPPPPP               LLLLLLLLLLLLLLLLLLLLLLLL     EEEEEEEEEEEEEEEEEEEEEE           TTTTTTTTTTT           EEEEEEEEEEEEEEEEEEEEEE
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
""")

time.sleep(100)
#makes the shell wait 10 secconds before closing


