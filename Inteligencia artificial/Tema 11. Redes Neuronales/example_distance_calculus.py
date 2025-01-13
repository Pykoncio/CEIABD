from neuron import Neuron

while True:

    hours = input("Enter the number of hours elapsed (Can contain decimal values) or type 'exit' to quit: ")
    if hours.lower() == "exit":
        break
    try:
        hours = float(hours)
    except ValueError:
        print("Please enter a valid number or 'exit' to quit.")
        continue

    neuron = Neuron(weights=[100], bias=60)
    km = neuron.run([hours])
    print(f"The vehicle has traveled {km} kilometers.")