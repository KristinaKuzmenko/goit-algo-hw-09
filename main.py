import timeit


def find_coins_greedy(total_sum, coins):
    # Сортуємо монети за номіналом за спаданням і починаємо ітерацію з монети з найбільшим номіналом
    coins = sorted(coins, reverse=True)
    coins_count = {}
    for coin in coins:
        if coin <= total_sum:
            coins_count[coin] = total_sum // coin
            total_sum %= coin
    return coins_count


def find_min_coins(total_sum, coins):
    # Сортуємо монети за номіналом за зростанням і починаємо ітерацію з монети з найменшим номіналом
    coins = sorted(coins)
    # Ініціалізація таблиці для динамічного програмування
    dp_table = [{} for _ in range(total_sum + 1)]
    dp_table[0] = {coin: 0 for coin in coins}
    for coin in coins:
        for change in range(1, total_sum + 1):
            if (
                coin <= change
            ):  # Якщо номінал монети не перевищує суму, перевіряємо, чи доцільно її використати
                remaining_change = change - coin
                # Копіюємо словник мінімальних кількостей монет для залишкової суми
                temp_change_dict = dp_table[remaining_change].copy()
                # Додаємо монету, збільшуючи кількість для цієї монети в словнику на 1
                temp_change_dict[coin] = temp_change_dict.get(coin, 0) + 1
                # Якщо словника для даної суми ще немає, або кількість монет зменшується при додаванні нової монети, оновлюємо словник
                if not dp_table[change] or sum(temp_change_dict.values()) < sum(
                    dp_table[change].values()
                ):
                    dp_table[change] = temp_change_dict

    return {
        coin: quantity for coin, quantity in dp_table[total_sum].items() if quantity > 0
    }


def dict_to_string(dictionary):
    return ", ".join(f"{key}: {value}" for key, value in dictionary.items())


# Тестування
if __name__ == "__main__":
    coins_1 = [50, 25, 10, 5, 2, 1]
    coins_2 = [60, 50, 25, 10, 5, 2, 1]
    total_sum_1 = 113
    total_sum_2 = 150
    total_sum_3 = 3678

    time_greedy = timeit.timeit(
        lambda: find_coins_greedy(total_sum_1, coins_1), number=1000
    )
    time_dynamic = timeit.timeit(
        lambda: find_min_coins(total_sum_1, coins_1), number=1000
    )

    time_greedy_bigdata = timeit.timeit(
        lambda: find_coins_greedy(total_sum_3, coins_1), number=1000
    )
    time_dynamic_bigdata = timeit.timeit(
        lambda: find_min_coins(total_sum_3, coins_1), number=1000
    )
    result_greedy_1 = dict_to_string(find_coins_greedy(total_sum_1, coins_1))
    result_dynamic_1 = dict_to_string(find_min_coins(total_sum_1, coins_1))
    result_greedy_2 = dict_to_string(find_coins_greedy(total_sum_2, coins_2))
    result_dynamic_2 = dict_to_string(find_min_coins(total_sum_2, coins_2))
    result_greedy_3 = dict_to_string(find_coins_greedy(total_sum_3, coins_1))
    result_dynamic_3 = dict_to_string(find_min_coins(total_sum_3, coins_1))

    print(f"| {'Algorithm':<30} | {'Greedy':^35} | {'Dynamic':^35} |")
    print(f"| {'-'*30} | {'-'*35} | {'-'*35} |")
    print(f"| {'Example 1':<30} | {result_greedy_1:<35} | {result_dynamic_1:<35} |")
    print(f"| {'Example 2':<30} | {result_greedy_2:<35} | {result_dynamic_2:<35} |")
    print(f"| {'Example 3':<30} | {result_greedy_3:<35} | {result_dynamic_3:<35} |")
    print(f"| {'-'*30} | {'-'*35} | {'-'*35} |")
    print(
        f"| {'Time for smaller sum':<30} | {time_greedy:^35.5f} | {time_dynamic:^35.5f} |"
    )
    print(
        f"| {'Time for bigger sum':<30} | {time_greedy_bigdata:^35.5f} | {time_dynamic_bigdata:^35.5f} |"
    )
