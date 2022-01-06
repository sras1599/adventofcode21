from collections import Counter

from parse_input import parse_input

with open("input") as file:
    numbers = parse_input(file)

numbers_to_consider_for_oxygen_rating = numbers.copy()
current_index = 0

while len(numbers_to_consider_for_oxygen_rating) > 1:
    most_common_numbers_at_current_index = Counter(
        map(lambda x: x[current_index], numbers_to_consider_for_oxygen_rating)
    ).most_common()

    if len(most_common_numbers_at_current_index) == 2:
        most_common, most_common_count = (
            most_common_numbers_at_current_index[0][0],
            most_common_numbers_at_current_index[0][1],
        )
        second_most_common, second_most_common_count = (
            most_common_numbers_at_current_index[1][0],
            most_common_numbers_at_current_index[1][1],
        )

        most_common = "1" if most_common_count == second_most_common_count else most_common
    else:
        most_common = most_common_numbers_at_current_index[0][0]

    numbers_to_consider_for_oxygen_rating = list(
        filter(lambda x: x[current_index] == most_common, numbers_to_consider_for_oxygen_rating)
    )
    current_index += 1


numbers_to_consider_for_co2_scrubber_rating = numbers.copy()
current_index = 0

while len(numbers_to_consider_for_co2_scrubber_rating) > 1:
    least_common_numbers_at_current_index = sorted(
        Counter(map(lambda x: x[current_index], numbers_to_consider_for_co2_scrubber_rating)).most_common(),
        key=lambda x: x[1],
    )

    if len(least_common_numbers_at_current_index) == 2:
        least_common, least_common_count = (
            least_common_numbers_at_current_index[0][0],
            least_common_numbers_at_current_index[0][1],
        )
        second_least_common, second_least_common_count = (
            least_common_numbers_at_current_index[1][0],
            least_common_numbers_at_current_index[1][1],
        )

        least_common = "0" if least_common_count == second_least_common_count else least_common
    else:
        least_common = least_common_numbers_at_current_index[0][0]

    numbers_to_consider_for_co2_scrubber_rating = list(
        filter(lambda x: x[current_index] == least_common, numbers_to_consider_for_co2_scrubber_rating)
    )
    current_index += 1


oxygen_rating = int(numbers_to_consider_for_oxygen_rating[0], 2)
co2_scrubber_rating = int(numbers_to_consider_for_co2_scrubber_rating[0], 2)

print(oxygen_rating * co2_scrubber_rating)
