from __future__ import annotations

from functools import reduce
from operator import mul
from typing import List, NamedTuple

from parse_input import parse_input


class Packet(NamedTuple):
    version: int
    type_id: int
    size: int
    content: List[Packet] | int


class Transmission:
    def __init__(self, message: str) -> None:
        self.message = message

    def decode(self) -> Packet:
        version = binary_string_to_int(self.truncate_message(3))
        type_id = binary_string_to_int(self.truncate_message(3))
        size = 6
        content = []

        if type_id == 4:
            while True:
                starting_digit, *value = self.truncate_message(5)
                size += 5
                content.extend(value)

                if starting_digit == "0":
                    break

            content = binary_string_to_int("".join(content))
        else:
            length_type_id = int(self.truncate_message(1))
            size += 1

            if length_type_id == 0:
                length_of_sub_packets_in_bits = binary_string_to_int(self.truncate_message(15))
                current_length_of_sub_packets = 0
                size += 15 + length_of_sub_packets_in_bits

                while current_length_of_sub_packets < length_of_sub_packets_in_bits:
                    sub_packet = self.decode()
                    content.append(sub_packet)
                    current_length_of_sub_packets += sub_packet.size
            else:
                number_of_sub_packets = binary_string_to_int(self.truncate_message(11))
                size += 11
                for _ in range(number_of_sub_packets):
                    sub_packet = self.decode()
                    content.append(sub_packet)
                    size += sub_packet.size

        return Packet(version, type_id, size, content)

    def truncate_message(self, by: int) -> str:
        val = self.message[:by]
        self.message = self.message[by:]

        return val


def binary_string_to_int(string: str) -> int:
    return int(string, base=2)


def hex_to_binary(hexadecimal_string: str):
    fill = len(hexadecimal_string) * 4

    return f"{int(hexadecimal_string, 16):08b}".zfill(fill)


def evalutate_expression(packet: Packet) -> int:
    if packet.type_id == 4:
        return packet.content

    values = [evalutate_expression(packet) for packet in packet.content]

    if packet.type_id == 0:
        return sum(values)
    elif packet.type_id == 1:
        return reduce(mul, values)
    elif packet.type_id == 2:
        return min(values)
    elif packet.type_id == 3:
        return max(values)
    elif packet.type_id == 5:
        return int(values[0] > values[1])
    elif packet.type_id == 6:
        return int(values[0] < values[1])
    else:
        return int(values[0] == values[1])


def main():
    with open("input", "r") as file:
        message = hex_to_binary(parse_input(file))
    transmission = Transmission(message)

    outermost_packet = transmission.decode()
    print(evalutate_expression(outermost_packet))


if __name__ == "__main__":
    main()
