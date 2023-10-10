from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency="USD")
        bot.select_place_to_go(input("Location to go: "))
        bot.select_data_to_go(check_in=input("Check in date: ")
                              ,check_out=input("Check out date: "))
        bot.select_adults(int(input(" Number of people: ")))
        bot.click_search()
        bot.appply_filtration()
        bot.refresh()
        bot.report_results()
except Exception as e:
        print("There is a problem running this program from command line  ")
    
   
    