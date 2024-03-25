from datetime import datetime
from zoneinfo import ZoneInfo

# Get the current time and date
now = datetime.now()
# Format the string as "9:27PM on March, 15 2024"
formatted_now = now.strftime("%I:%M %p on %B, %d %Y")

# Print the formatted string
print("\nKarl's Time Convergence App Initializing on...")

print(formatted_now)
print("\n")


def arizona_to_est(arizona_time_str):
    # Get the current date in the 'YYYY-MM-DD' format
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Combine the current date with the input time
    datetime_str = f"{current_date} {arizona_time_str}"

    # Define the Arizona and Eastern time zones
    arizona_zone = ZoneInfo("America/Phoenix")
    eastern_zone = ZoneInfo("US/Eastern")

    # Parse the input datetime string with standard AM/PM format
    arizona_time = datetime.strptime(datetime_str, '%Y-%m-%d %I:%M %p')

    # Assign the Arizona timezone to the datetime object
    arizona_time = arizona_time.replace(tzinfo=arizona_zone)

    # Convert to Eastern Time
    est_time = arizona_time.astimezone(eastern_zone)

    # Format the Eastern Time to only display the time in standard AM/PM format, without the date
    return est_time.strftime('%I:%M %p %Z%z')


# Example usage
arizona_time_str = "12:00 PM"  # An example Arizona time without the date
est_time_str = arizona_to_est(arizona_time_str)
print(f"{arizona_time_str} Arizona Time is {est_time_str} Eastern Time")
