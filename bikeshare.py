import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ["january","feburary","march","april","may","june"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington)
    city = input('Would you like to see data for Chicago, New York, or Washington?\n').lower()
    while(True):
        if city in CITY_DATA:
            break;
        else:
            city =input('You entered wrong city. Enter correct city\n\n').lower()
    #value of month day is none by default "none". ****there is difference between "none" and None
    month = "none"
    day = "none"
    # Asking user whether he wants any kind of filtering or not
    filter_ = input("Would you like to filter data by month, day, both or not at all ? Enter none for no filtering\n").lower()
    #loop to check whether filter_ value is month, day, both or none  if not then ask user  to enter correct value
    
    while(True):
        if(filter_ == "month"):
            month = input("\nWhich month- January, Feburary, March, April, May or June ?\n").lower()
             # if month is valid then break else ask user to enter correct month
            while True:
                if(month in months):
                    break
                else:
                    month = input("You entered wrong month. Please choose month from January, Feburary, March, April, May or June\n").lower()
        elif(filter_ == "day"):
            day = input("\nWhich Day ? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday\n").lower()
            # check if entered day is correct or not, if not then ask user to enter valid day
            while(True):
                if (day in ('monday','sunday','tuesday','thursday','wednesday','friday','saturday')):
                    break;
                else:
                    day = input("You entered wrong number for day. Which Day ?\n").lower()                      
        elif(filter_ == "both"):
            month = input("\nWhich month- January, Feburary, March, April, May or June ?\n").lower()
            # break if entered month is valid else ask user to enter valid month
            while True:
                if(month in months):
                    break
                else:
                    month = input("You entered wrong month. Please choose month from January, Feburary, March, April, May or June\n").lower()
            day = input("\nWhich Day ? Sunday, Monday,Tuesday, Wednesday, Thursday, Friday, Saturday\n").lower()
            # break if user entered corrected day else ask user to enter valid date
            while(True):
                if (day in ('monday','sunday','tuesday','thursday','wednesday','friday','saturday')):
                    break;
                else:
                    day = input("You entered wrong number for day. Which Day ?\n").lower()   
        elif(filter_ == "none"):
            day = "none"
            month = "none"
            break
        else :
            filter_ = input("You entered wrong option. Would you like to filter data by month, day, both or not at all ? Enter none for no filtering\n").lower()
            continue
        break
    print('-'*40)
    
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "none" to apply no month filter
        (str) day - name of the day of week to filter by, or "none" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'none':
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'none':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print("calculating statistics")
    # display the most common month
    common_month = df['month'].mode() [0]
    print('Most Common Month:', common_month)
    
    # display the most common day of week
    common_day = df['day_of_week'].mode() [0]
    print('Most Common Day of Week:', common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly used start station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Commonly used end station:', common_end_station)

    # display most frequent combination of start station and end station trip
    # it is done to concat start and end station then to find mode
    most_frequent_combination = df['Start Station']+" - "+df['End Station']
    most_frequent_combination = most_frequent_combination.mode()[0]
    print("Most frequent combination of start and end station trip are  ", most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    tt = sum(df['Trip Duration'])
    # to convert seconds into days. It is divided by (60*60*24 = 86400)
    print('Total travel time: {} Days'.format(tt/86400))
    mean_tt = df['Trip Duration'].mean()
    print('Mean travel time: {} minutes'.format(mean_tt/60))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #  Display counts of user types
    usertype_count = df["User Type"].value_counts()
    print("User count by type", usertype_count)
    # Display counts of gender
    if "Gender" in df.columns:
        gender_count = df["Gender"].value_counts()
        print("Gender Count ",gender_count)
        # isna() is a method which returns rows in form of true or false.True if it contains missing value else false. sum() is used to count null entries
        null_entries = df["Gender"].isna().sum()
        if(null_entries>0):
            print("There are ", null_entries," NaN values")
    else:
        print("No information regarding gender is there in the dataset\n")

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print("Earliest year : ", int(earliest_year))
        print("Most Recent year : ", int(most_recent_year))
        print("Most Common year : ", int(most_common_year))
    else:
        print("No information of birth year is there in dataset\n")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_function(df):
    choice = input("\nDo you want to see raw data ?\n enter y for yes and n for no\n").lower()
    index = 0
    while(True):
        print(df.iloc[index : index+5])
        choice = input("\nDo you want to see more raw data ?\n enter y for yes and n for no\n").lower()
        if(choice == "n"):
            break
        index = index+5
    print('-'*40)   
                      
                      

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_function(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
 
if __name__ == "__main__":
	main()
