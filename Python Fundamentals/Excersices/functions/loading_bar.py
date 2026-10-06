def create_loading_bar(percents:int ):
    if percents ==100:
        return print("100% Complete!\n[%%%%%%%%%%]")

    return print(f"{percents}% [{'%' * (percents//10)}{'.' * (10 - (percents//10))}]\nStill loading...")
number = int(input())
create_loading_bar(number)