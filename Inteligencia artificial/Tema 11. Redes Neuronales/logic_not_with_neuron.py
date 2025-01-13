from neuron import Neuron

logic_not = Neuron(weights=[-1], bias=0.5, activation_function_name="binary_step")

print(logic_not.run([0])) # 1
print(logic_not.run([1])) # 0