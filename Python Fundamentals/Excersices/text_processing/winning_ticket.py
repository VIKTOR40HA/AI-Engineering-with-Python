tickets = input().split(", ")

for ticket in tickets:
    ticket = ticket.strip()

    if len(ticket) != 20:
        print("invalid ticket")
        continue

    left_half = ticket[:10]
    right_half = ticket[10:]
    winning_symbols = "@#$^"
    best_symbol = ""
    best_length = 0

    for symbol in winning_symbols:
        left_match = len(left_half) - len(left_half.rstrip(symbol))
        right_match = len(right_half) - len(right_half.rstrip(symbol))

        left_start = len(left_half) - len(left_half.lstrip(symbol))
        right_start = len(right_half) - len(right_half.lstrip(symbol))

        left_length = max(left_match, left_start)
        right_length = max(right_match, right_start)

        if left_length >= 6 and right_length >= 6:
            match_length = min(left_length, right_length)

            if match_length > best_length:
                best_length = match_length
                best_symbol = symbol

    if best_length == 0:
        print(f'ticket "{ticket}" - no match')
    elif best_length == 10:
        print(f'ticket "{ticket}" - 10{best_symbol} Jackpot!')
    else:
        print(f'ticket "{ticket}" - {best_length}{best_symbol}')