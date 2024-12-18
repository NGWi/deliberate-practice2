class Address:
    def __init__(self, number, street, city, state) -> None:
        self.number = number
        self.street = street
        self.city = city
        self.state = state

def build_index(address_book: list[Address]):
    number_index, street_index, city_index, state_index = {}, {}, {}, {}
    for idx, address in enumerate(address_book):
        # Populate number index
        if address.number is not None:
            if address.number not in number_index:
                number_index[address.number] = set()
            number_index[address.number].add(idx)

        # Populate street index
        if address.street is not None:
            if address.street not in street_index:
                street_index[address.street] = set()
            street_index[address.street].add(idx)

        # Populate city index
        if address.city is not None:
            if address.city not in city_index:
                city_index[address.city] = set()
            city_index[address.city].add(idx)

        # Populate state index
        if address.state is not None:
            if address.state not in state_index:
                state_index[address.state] = set()
            state_index[address.state].add(idx)

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

# Test code:

from faker import Faker
import random

if __name__ == "__main__":
    fake = Faker()

    address_book = [Address(fake.building_number(), fake.street_name(), fake.city(), fake.state_abbr()) for _ in range(100)]
    for address in address_book:
        print(f"{address.number} {address.street}, {address.city}, {address.state}")

    number_index, street_index, city_index, state_index = build_index(address_book)
    print(number_index)
    print(street_index)
    print(city_index)
    print(state_index)

    test_cases = [Address(
        random.choice(list(number_index.keys())) if random.choice([True, False]) else None,
        random.choice(list(street_index.keys())) if random.choice([True, False]) else None,
        random.choice(list(city_index.keys())) if random.choice([True, False]) else None,
        random.choice(list(state_index.keys())) if random.choice([True, False]) else None
    ) for _ in range(100)]

    for query in test_cases:
        print(f"Search for {query.number}, {query.street}, {query.city}, {query.state}")
        result = search(query)
        print(f"Result: {result}")