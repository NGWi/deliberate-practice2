class Address:
    def __init__(self, number, street, city, state) -> None:
        self.number = number
        self.street = street
        self.city = city
        self.state = state

def build_index(address_book: list[Address]):
    number_index, street_index, city_index, state_index = {}, {}, {}, {}
    for idx, address in enumerate(address_book):
        for prop_val, index_dict in (
            (address.number, number_index),
            (address.street, street_index),
            (address.city, city_index),
            (address.state, state_index),
        ):
            if prop_val is not None:
                if prop_val not in index_dict:
                    index_dict[prop_val] = set()
                index_dict[prop_val].add(idx)

    return number_index, street_index, city_index, state_index

def search(search_query: Address) -> bool:
    filtered_indices = set()
    if not any(vars(search_query).values()):
        print("Please input a valid address.")
        return False

    # Start with the most unique property
    if search_query.number is not None:
        filtered_indices = number_index.get(search_query.number, set())
    else:
        filtered_indices = set(range(len(address_book)))  # All indices if number is None

    for index, prop in (
        (street_index, search_query.street),
        (city_index, search_query.city),
        (state_index, search_query.state),
    ):
        if prop is not None:
            filtered_indices &= index.get(prop, set())
            if not filtered_indices:
                return False
    else:
        return True

#---------------------------------------------------------------------------#
# Test code:

from faker import Faker
import random

if __name__ == "__main__":
    fake = Faker()

    address_book = [Address(fake.building_number(), fake.street_name(), fake.city(), fake.state_abbr()) for _ in range(5)]
    for address in address_book:
        print(f"{address.number} {address.street}, {address.city}, {address.state}")

    number_index, street_index, city_index, state_index = build_index(address_book)
    print(number_index)
    print(street_index)
    print(city_index)
    print(state_index)

    test_cases = [Address(
        random.choice(list(index.keys())) if random.choice([True, False]) else None
        for index in (number_index, street_index, city_index, state_index)
    ) for _ in range(20)]

    for query in test_cases:
        print(f"Search for {query.number}, {query.street}, {query.city}, {query.state}")
        result = search(query)
        print(f"Result: {result}")