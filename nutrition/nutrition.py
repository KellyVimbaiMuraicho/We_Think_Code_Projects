def main():
    
    fruit_choice = input("What type of fruit would you like to have ?").casefold()
    
    
    my_fruits ={"apple":"130","avocado":"50","banana":"110","cantaloupe":"50","grapefruits":"60","grapes":"90","honeybrew melon":"50","kiwifruit":"90","lemon":"15","lime":"20","nectarine":"60","orange":"80","peach":"60","pear":"100","pineapple":"50","plums":"70","strawberries":"50","sweet cherries":"100","tangerine":"50","watermelon":"80"}
    
    
    chosen_fruit = my_fruits.get(fruit_choice,"fruit not found ")
    
    if chosen_fruit != "fruit not found ":
        print(f"The fruit has {chosen_fruit} calories")
        
    else:
        print(chosen_fruit)
        
main()