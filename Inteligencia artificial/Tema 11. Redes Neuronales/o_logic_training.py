from neuron import Neuron
import numpy as np

training_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
training_outputs = np.array([0, 1, 1, 1])

w = np.random.rand(2)
b = np.random.rand(1)[0]

neuron = Neuron(w, b, activation_function_name="binary_step")

# Training parameters
learning_rate = 0.2
acceptable_e = 0.01
max_iterations = 10000

for iteration in range(max_iterations):
    total_e = 0

    for x, desired_y in zip(training_inputs, training_outputs):

        y = neuron.run(x)
        
        e = desired_y - y
        
        # Adjust the weights and bias
        neuron.weights += learning_rate * e * x
        neuron.bias += learning_rate * e
        
        # Accumulate the error
        # The error is accumulated in absolute terms to measure the magnitude of the error, 
        # regardless of its direction
        total_e += abs(e)
    
    # Check if the error is acceptable
    if total_e / len(training_inputs) < acceptable_e:
        print(f"Training completed in {iteration+1} iterations.")
        break
else:
    print("Training did not converge")


print("Final weights:", neuron.weights)
print("Final bias:", neuron.bias, end="\n\n")

print(neuron.run([0, 0]))
print(neuron.run([0, 1]))
print(neuron.run([1, 0]))
print(neuron.run([1, 1]))