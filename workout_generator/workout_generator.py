import random

# Sample workout database
workouts = {
    "cardio": [
        "Jumping Jacks",
        "Burpees",
        "High Knees",
        "Mountain Climbers",
        "Butt Kicks",
        "Skipping Rope"
    ],
    "strength": [
        "Push-ups",
        "Squats",
        "Lunges",
        "Plank",
        "Deadlifts",
        "Bicep Curls"
    ],
    "flexibility": [
        "Forward Bend",
        "Side Stretch",
        "Cat-Cow Pose",
        "Cobra Stretch",
        "Seated Forward Bend",
        "Child's Pose"
    ]
}

warm_up = ["Arm Circles", "Leg Swings", "Shoulder Rolls"]
cool_down = ["Deep Breathing", "Neck Stretch", "Hamstring Stretch"]

# Function to calculate total workout duration
def calculate_total_duration(num_exercises, duration_per_exercise, rest_time, has_warmup_cooldown=True):
    total_time = num_exercises * (duration_per_exercise + rest_time)
    if has_warmup_cooldown:
        total_time += 2 * (len(warm_up) + len(cool_down)) * 15  # Assuming 15 seconds per warm-up/cooldown exercise
    return total_time

# Function to generate a workout plan
def generate_workout(workout_type, num_exercises, duration_per_exercise=30, rest_time=10):
    # Constraints for workout
    max_exercises = min(6, len(workouts[workout_type]))  # Limit to 6 or the number available
    min_duration = 10  # Minimum duration per exercise
    max_duration = 60  # Maximum duration per exercise
    max_rest_time = 30  # Maximum rest time

    # Enforcing constraints
    num_exercises = min(max_exercises, max(1, num_exercises))
    duration_per_exercise = max(min_duration, min(max_duration, duration_per_exercise))
    rest_time = max(0, min(max_rest_time, rest_time))

    if workout_type not in workouts:
        print(f"Sorry, we don't have workouts for '{workout_type}'. Try 'cardio', 'strength', or 'flexibility'.")
        return

    exercises = random.sample(workouts[workout_type], min(num_exercises, len(workouts[workout_type])))
    total_duration = calculate_total_duration(num_exercises, duration_per_exercise, rest_time)
    
    print(f"\nYour {workout_type.capitalize()} Workout Plan (Approx. {total_duration // 60} min):")
    print("\nWarm-Up:")
    for i, exercise in enumerate(warm_up, 1):
        print(f"{i}. {exercise} - 15 seconds")
    
    print("\nMain Workout:")
    for i, exercise in enumerate(exercises, 1):
        print(f"{i}. {exercise} - {duration_per_exercise} seconds")
        if i < num_exercises:
            print(f"   Rest - {rest_time} seconds")
    
    print("\nCooldown:")
    for i, exercise in enumerate(cool_down, 1):
        print(f"{i}. {exercise} - 15 seconds")

# Function to create a mixed workout plan
def generate_mixed_workout(num_exercises, duration_per_exercise=30, rest_time=10):
    # Constraints for workout
    max_exercises = 10  # Limit to 10 exercises for mixed workouts
    min_duration = 10  # Minimum duration per exercise
    max_duration = 60  # Maximum duration per exercise
    max_rest_time = 30  # Maximum rest time

    # Enforcing constraints
    num_exercises = min(max_exercises, max(1, num_exercises))
    duration_per_exercise = max(min_duration, min(max_duration, duration_per_exercise))
    rest_time = max(0, min(max_rest_time, rest_time))

    all_exercises = []
    for workout_type in workouts:
        all_exercises.extend(workouts[workout_type])

    exercises = random.sample(all_exercises, min(num_exercises, len(all_exercises)))
    total_duration = calculate_total_duration(num_exercises, duration_per_exercise, rest_time)
    
    print(f"\nYour Mixed Workout Plan (Approx. {total_duration // 60} min):")
    print("\nWarm-Up:")
    for i, exercise in enumerate(warm_up, 1):
        print(f"{i}. {exercise} - 15 seconds")
    
    print("\nMain Workout:")
    for i, exercise in enumerate(exercises, 1):
        print(f"{i}. {exercise} - {duration_per_exercise} seconds")
        if i < num_exercises:
            print(f"   Rest - {rest_time} seconds")
    
    print("\nCooldown:")
    for i, exercise in enumerate(cool_down, 1):
        print(f"{i}. {exercise} - 15 seconds")

# User input with constraints
print("Welcome to the Enhanced Workout Generator!")
mode = input("Choose mode (single type, mixed): ").strip().lower()

if mode == "single type":
    workout_type = input("Enter workout type (cardio, strength, flexibility): ").strip().lower()
    num_exercises = int(input("Enter the number of exercises (1-6): "))
    duration = int(input("Enter the duration for each exercise (10-60 seconds): "))
    rest_time = int(input("Enter rest time between exercises (0-30 seconds): "))
    generate_workout(workout_type, num_exercises, duration, rest_time)

elif mode == "mixed":
    num_exercises = int(input("Enter the number of exercises (1-10): "))
    duration = int(input("Enter the duration for each exercise (10-60 seconds): "))
    rest_time = int(input("Enter rest time between exercises (0-30 seconds): "))
    generate_mixed_workout(num_exercises, duration, rest_time)
else:
    print("Invalid mode. Please choose 'single type' or 'mixed'.")
