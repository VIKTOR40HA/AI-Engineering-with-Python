CHIKEN_MENU = 10.35
FISH_MENU = 12.40
VEGETARIAN_MENU = 8.15

chiken_menu_count=int(input())
fish_menu_count=int(input())
vegetarian_menu_count=int(input())

menus = chiken_menu_count * CHIKEN_MENU + fish_menu_count * FISH_MENU + vegetarian_menu_count * VEGETARIAN_MENU
desert = menus*0.2
total = menus + desert + 2.5
print(total)
