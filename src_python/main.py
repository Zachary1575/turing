from protobuf import example_pb2

# Lets try to write one thing in this file and then push out organically.
def parse(expression) -> None:
    print(f"Given Expression: {expression}")

    # Do some stuff with the expression
    # ...
    # ...
    # ...

    # Then we package it up with the serializer provided by protoc
    person = example_pb2.Person()
    person.name = "Alice"
    person.id = 1
    person.email = "alice@hotmail.com"

    # Serialize into bytes
    data = person.SerializeToString()
    print(f"Byte Data: ${data}")

    # Then slap it into in-memory

    print("Operation Done.")
    return


def main() -> None:
    print("Ayyy!")
    return

main()