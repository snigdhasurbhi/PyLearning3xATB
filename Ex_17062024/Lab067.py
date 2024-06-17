def make_pizza(*toppings, base):
    """Print the list of toppings that have been requested."""
    print(toppings)
    print(base)
    print("Make your pizza!")
    for topping in toppings:
        print(f"Adding {topping} to your pizza.")
        print(f"Your pizza base is {base}.")
amit=make_pizza("mushroom","tomato","onion","olives",base="thin crust")
dev=make_pizza("paneer", "sweetcorn", "pineapple", base="thick crust")
shaiv=make_pizza("capsicum", base="thin crust")