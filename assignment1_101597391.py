"""
Author: Jocelyn Brown
Assignment: #1
"""

# -------------------------------------------------------------------------------------------------------------------------------------------
# Step b: Create 4 variables:
gym_member = "Alix Alliton" # Data Type: String
preferred_weight_kg = 20.5  # Data Type: Float
highest_reps = 25           # Data Type: Integer
membership_active = True    # Data Type: Boolean

# -------------------------------------------------------------------------------------------------------------------------------------------
# Step c: Create a dictionary named workout_stats:
# Dictionary: Keys are Strings (friend names)
# Values are Tuples containing three Integers (yoga, running, weightlifting minutes)
workout_stats = {
    "Alex": (30, 45, 60), 
    "Katherine": (20, 35, 40),
    "Marina": (25, 30, 55),
    "Fabio": (15, 20, 25)
}

# -------------------------------------------------------------------------------------------------------------------------------------------
# Step d: Calculate total workout minutes using a loop and add to dictionary: 
for friend, minutes in list(workout_stats.items()): # Loop through the workout_stats dictionary to access each friend's name and their corresponding workout minutes.
    workout_stats[f"{friend}_Total"] = sum(minutes) # Calculate the total workout minutes by summing the tuple of minutes for each friend and add a new key-value pair to the dictionary with the key as "{friend}_Total" and the value as the calculated total workout minutes.

# -------------------------------------------------------------------------------------------------------------------------------------------
# Step e: Create a 2D nested list called workout_list:
# 2D Nested List: List of Lists containing workout minutes (Integers)
# Each row represents one friend, columns represent yoga, running, and weightlifting minutes respectively
workout_list = []
friend_names = []

for friend, minutes in workout_stats.items(): # Loop through the workout_stats dictionary to access each friend's name and their corresponding workout minutes.
    if not friend.endswith("_Total"):         # Only include friends' workout minutes, not totals.
        friend_names.append(friend)           # Keep track of friend names for reference.
        workout_list.append(list(minutes))    # Convert the tuple of minutes to a list and add to workout_list.

# -------------------------------------------------------------------------------------------------------------------------------------------
# Step f: Slice the workout_list Slice the workout_list to:
# Extract and print the minutes for yoga and running for all friends:
print("Yoga and Running Minutes for All Friends:")
for i in range(len(workout_list)):                                     # Loop through each row of workout_list to access the yoga and running minutes for all friends.
    print(f"{friend_names[i]}: Yoga = {workout_list[i][0]} minutes, "  # Print the name of the friend along with their yoga and running minutes.
           f"Running = {workout_list[i][1]} minutes")

# Extract and print the minutes for weightlifting for the last two friends:
print("\nWeightlifting Minutes for Last Two Friends:")
for i in range(-2, 0):                           # Loop through the last two rows of workout_list to access the weightlifting minutes for the last two friends.
    print(f"{friend_names[i]}: Weightlifting = " # Print the name of the friend along with their weightlifting minutes.
          f"{workout_list[i][2]} minutes")

# -------------------------------------------------------------------------------------------------------------------------------------------
# Step g: Check if any friend's total >= 120 ".
print("\nFriends with Total Workout Minutes >= 120:") 
for friend in friend_names: # Loop through the list of friend names to access their total workout minutes from the dictionary.
    total_minutes = workout_stats[f"{friend}_Total"] 
    if total_minutes >= 120:                          # Check if the total workout minutes for the current friend is greater than or equal to 120.
        print(f"Great job staying active, {friend}!") # Print a congratulatory message for the friend if their total workout minutes is greater than or equal to 120.

# -------------------------------------------------------------------------------------------------------------------------------------------
# Step h: User input to look up a friend.
# Add a feature to allow the user to input a friend's name. Check if the name exists in the dictionary:
user_input = input("\nEnter a friend's name to look up their workout details: ") # Prompt the user to enter a friend's name to look up their workout details.

if user_input in workout_stats and not user_input.endswith("_Total"): # Ensure we are checking for a friend's name, not a total key.
    yoga, running, weightlifting = workout_stats[user_input]          # Unpack the tuple of workout minutes for the specified friend.
    total = workout_stats[f"{user_input}_Total"]                      # Retrieve the total workout minutes for the specified friend.
    print(f"{user_input}'s Workout Details:")        # Print the workout details for the specified friend.
    print(f"Yoga: {yoga} minutes")                   # Print the yoga minutes for the specified friend.
    print(f"Running: {running} minutes")             # Print the running minutes for the specified friend.
    print(f"Weightlifting: {weightlifting} minutes") # Print the weightlifting minutes for the specified friend.
    print(f"Total workout minutes: {total}")         # Print the total workout minutes for the specified friend.
else:
    print(f"Friend {user_input} not found in the records.") # Inform the user if the entered friend's name does not exist in the dictionary.
    
# -------------------------------------------------------------------------------------------------------------------------------------------
# Step i: Friend with highest and lowest total workout minutes.
highest_total = 0           # Initialize to 0 since we are looking for the maximum value.
lowest_total = float('inf') # Initialize to infinity to ensure any total will be lower than this initial value when we look for the minimum.

highest_friend = "" # Initialize to an empty string to store the name of the friend with the highest total workout minutes.
lowest_friend = ""  # Initialize to an empty string to store the name of the friend with the lowest total workout minutes.

for friend in friend_names: # Loop through the list of friend names to access their total workout minutes from the dictionary.
    total_minutes = workout_stats[f"{friend}_Total"]

    if total_minutes > highest_total: # Check if the current friend's total workout minutes is greater than the highest total found so far.
        highest_total = total_minutes # Update the highest total workout minutes if the current friend's total is greater.
        highest_friend = friend       # Update the name of the friend with the highest total workout minutes.

    if total_minutes < lowest_total:  # Check if the current friend's total workout minutes is less than the lowest total found so far.
        lowest_total = total_minutes  # Update the lowest total workout minutes if the current friend's total is lower.
        lowest_friend = friend        # Update the name of the friend with the lowest total workout minutes.
    
print(f"\nFriend with the highest total workout minutes: " # Print the name of the friend with the highest total workout minutes along with the total minutes.
       f"{highest_friend} ({highest_total} minutes)")

print(f"Friend with the lowest total workout minutes: "    # Print the name of the friend with the lowest total workout minutes along with the total minutes.
       f"{lowest_friend} ({lowest_total} minutes)")
