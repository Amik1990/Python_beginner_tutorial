from Chef import Chef

# Abychom nemusel vypisovat stejné funkce z Chef souboru tak je zdědíme. Do závorky třídy napíšeme název souboru, ze kterého chceme dědit. Zde je to Chef
class ChineseChef(Chef):

    def make_special_dish(self):
        print("The chef makes orange chicken")
    def make_fried_rice(self):
        print("The chef makes fried rice")
