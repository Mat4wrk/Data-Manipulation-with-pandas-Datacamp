#Create a DataFrame called individuals that contains only the individuals column of homelessness.
#Print the head of the result.

# Select the individuals column
individuals = homelessness["individuals"]

# Print the head of the result
print(individuals.head())


#Create a DataFrame called state_fam that contains only the state and family_members columns of homelessness, in that order.
#Print the head of the result.

# Select the state and family_members columns
state_fam = homelessness[["state", "family_members"]]

# Print the head of the result
print(state_fam.head())


#Create a DataFrame called ind_state that contains the individuals and state columns of homelessness, in that order.
#Print the head of the result.

# Select only the individuals and state columns, in that order
ind_state = homelessness[["individuals", "state"]]

# Print the head of the result
print(ind_state.head())
