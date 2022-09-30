import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    #Asks user to specify a city, month, and day to analyze.

    #Returns:
#        (str) city - name of the city to analyze
    #    (str) month - name of the month to filter by, or "all" to apply no month filter
        #(str) day - name of the day of week to filter by, or "all" to apply no day filter
#    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # ask user for city of interest, using lower method to make it case insensitive.
    city = input('What city do you want to see data from? Choose one of these 3 options: chicago, new york city or washington: ').lower()
    # use while loop so that the user is asked the same question until a valid value is entered
    while (city != 'chicago') and (city != 'new york city') and (city !='washington'):
        city = input ("Your input is not valid. Choose one of these please: chicago, new york city or washington: ").lower()

    # get user input for month (all, january, february, ... , june)
    # ask user for month of interest, using lower method to make it case insensitive.
    month = input('What month do you want to see data from? Choose one of these options: all, january, february, march, april, may or june: ').lower()
    # use while loop so that the user is asked the same question until a valid value is entered
    while (month !='all') and (month !='january') and (month != 'february') and (month !='march') and (month != 'april') and (month != 'may') and (month != 'june'):
        month = input('Your input is not valid. Choose one of these options: all, january, february, march, april, may or june: ').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    # ask user for day of interest, using lower method to make it case insensitive.

    day = input('What day do you want to see data from? Choose one of these options: all, monday, tuesday, wednesday, thursday, friday, saturday or sunday: ').lower()
    # use while loop so that the user is asked the same question until a valid value is entered
    while (day != 'monday') and (day != 'tuesday') and (day != 'wednesday') and (day != 'thursday') and (day != 'friday') and (day != 'saturday') and (day != 'sunday') and (day != 'all'):
        day = input('Your input is not valid. Choose one of these options: all, monday, tuesday, wednesday, thursday, friday, saturday or sunday: ').lower()

    print('-'*40)
    return city, month, day

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    #Loads data for the specified city and filters by month and day if applicable.

    #Args:
        #(str) city - name of the city to analyze
        #(str) month - name of the month to filter by, or "all" to apply no month filter
        #(str) day - name of the day of week to filter by, or "all" to apply no day filter
#    Returns:
        #df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    #change columns to date format yyyy-mm-dd
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    # create columns of month, day of week and hour using start time.
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    # filter by month, when required
    if (month == 'january') or (month == 'february') or (month == 'march') or (month == 'april') or (month == 'may') or (month == 'june'):
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    # filter by day of month, when required
    if (day == 'monday') or (day == 'tuesday') or (day == 'wednesday') or (day == 'thursday') or (day == 'friday') or (day == 'saturday') or (day == 'sunday'):
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    #obtain the most common month, most common day and most common hour
    month_most_common = df['month'].mode()[0]
    day_most_common = df['day_of_week'].mode()[0]
    df['hour'] = df['Start Time'].dt.hour
    hour_most_common = df['hour'].mode()[0]

    # display the most common month
    print("The most common month is: {}".format(month_most_common))

    # display the most common day of week

    print("The most common day is: {}".format(day_most_common))

    # display the most common start hour

    print("The most common hour is: {}".format(hour_most_common))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station_most_common = df['Start Station'].mode()[0]

    print("Most common start station: {}".format(start_station_most_common))


    # display most commonly used end station
    end_station_most_common = df['End Station'].mode()[0]

    print("Most common end station: {}".format(end_station_most_common))


    # display most frequent combination of start station and end station trip

    most_common_start_end_stations = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).head(1)

    print("Most frequent combination of start station and end station trip: \n{}".format(most_common_start_end_stations))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    duration_total = df['Trip Duration'].sum()
    print("total travel time in seconds is: {}".format(duration_total))

    # display mean travel time
    duration_mean = df['Trip Duration'].mean()
    print("mean travel time in seconds is: {}".format(duration_mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print("Count of user types: \n{}".format(user_types_counts))

    # Washington doesn't have columns of birth year and gender, so an if statement is included

    if (city == 'chicago' or city == 'new york city'):


        # Display counts of gender
        user_gender_counts = df['Gender'].value_counts()
        print("Count of gender: \n{}".format(user_gender_counts))
        # Display earliest, most recent, and most common year of birth
        # Using the min module to obtain the minimum
        year_of_birth_earliest = df['Birth Year'].min()
        print("The earliest year of birth is: {}".format(year_of_birth_earliest))
        # Using the max module to obtain the maximum
        year_of_birth_most_recent = df['Birth Year'].max()
        print("The most recent year of birth is: {}".format(year_of_birth_most_recent))
        # Using the module module to obtain the most frequent
        year_of_birth_most_common = df['Birth Year'].mode()[0]
        print("The most frequent year of birth is: {}".format(year_of_birth_most_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data (df):
    row_number=0
    while True:
        view_raw_data_answer = input("Do you want to see the raw data? for 'Yes' enter 'Y' and for 'No' enter 'N'.\n").lower()

        if view_raw_data_answer == "y":
            print(df.iloc[row_number :row_number + 6])
            row_number += 6
        elif view_raw_data_answer == "n":
            break
        else:
            print("Please enter your answer correctly. For 'Yes' enter 'Y' and for 'No' enter 'N'")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        # the user can see new data if required
        display_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
