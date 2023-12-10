import pandas as pd
# Reading Dataframe
data=pd.read_csv(r"dataset-1.csv")

def generate_car_matrix(df):
  
  # Create a new DataFrame with id_2 as columns and id_1 as index.
  car_matrix = df.pivot_table(index='id_1', columns='id_2', values='car', fill_value=0)

  # Set diagonal values to 0.
  car_matrix.values[range(len(car_matrix)), range(len(car_matrix))] = 0

  return car_matrix

car_matrix = generate_car_matrix(data)
print(car_matrix)

def get_type_count(df):
    

    # Define car type categories and thresholds
    car_types = {
        "low": (-float("inf"), 15),
        "medium": (15, 25),
        "high": (25, float("inf")),
    }

    # Create a new column 'car_type' based on car values
    df["car_type"] = pd.cut(df["car"], bins=[-float("inf"), 15, 25, float("inf")], labels=list(car_types.keys()))

    # Count occurrences for each car type
    type_counts = df["car_type"].value_counts().to_dict()

    # Sort car type counts alphabetically
    sorted_counts = dict(sorted(type_counts.items()))

    return sorted_counts


type_counts = get_type_count(data)
print(type_counts)

def get_bus_indexes(df):
  

  # Calculate the mean value of the bus column
  mean_bus_value = df["bus"].mean()

  # Identify indices where bus values are greater than twice the mean
  bus_indexes = df[df["bus"] > 2 * mean_bus_value].index.tolist()

  # Sort the indices in ascending order
  bus_indexes.sort()

  return bus_indexes
# Get the indices where bus values are greater than twice the mean
bus_indexes = get_bus_indexes(data)

# Print the resulting list of indices
print(bus_indexes)

def filter_routes(dataframe):
    
    # Filter routes based on the condition
    filtered_routes = dataframe.groupby('route')['truck'].mean().loc[lambda x: x > 7].index.tolist()

    # Sort the list
    sorted_routes = sorted(filtered_routes)

    return sorted_routes
result_routes = filter_routes(data)
print(result_routes)

def multiply_matrix(input_matrix):
    
    # Create a deep copy to avoid modifying the original DataFrame
    modified_matrix = input_matrix.copy()

    # Apply the multiplication logic
    modified_matrix = modified_matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)

    # Round values to 1 decimal place
    modified_matrix = modified_matrix.round(1)

    return modified_matrix


result_matrix_modified = multiply_matrix(car_matrix)
print(result_matrix_modified)
