class MyClass:
    def __init__(self, data):
        self.data = data

# List to store instances of MyClass
instances = []

# Get the number of instances to create
num_instances = int(input("Enter the number of instances to create: "))

# Create instances with user-provided data
for i in range(num_instances):
    data = input(f"Enter data for instance {i + 1}: ")
    instance = MyClass(data)
    instances.append(instance)

# Access and use the instances
for i, instance in enumerate(instances):
    print(f"Data for instance {i + 1}: {instance.data}")
