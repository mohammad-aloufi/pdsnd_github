#This project provides some useful data and stats on a company called bikeshare. This company rents bikes to people for trips to an other station or to the same station if the person  was looking for a ride. You can get the datasets from udacity. The datasets are for chicago, new york city, and washington.
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    global city
    city=''
    city=city.lower()
    while(city!='chicago' or city!='new york city' or city!='washington'):
        city=input('Enter the city name you want to inquire about.\nchicago, new york city or washington')
        city=city.lower()
        if(city=='chicago' or city=='new york city' or city=='washington'):
            break


    # get user input for month (all, january, february, ... , june)
    global month
    month=''
    month=month.lower()
    while(month!='all' or month !='january' or month!='february' or month!='march' or month!='april' or month!='may' or month!='june'):
        month=input('Please enter the month, or enter \"all\" for all months.\nExample:\njanuary, february or march')
        month=month.lower()
        if(month=='all' or month =='january' or month =='february' or month =='march' or month =='april' or month =='may' or month =='june'):
                print('grate')
                break

    # get user input for day of week (all, monday, tuesday, ... sunday)

    global day
    day=''   
    day=day.lower()
    while(day!='all' or day !='sunday' or day !='monday' or day !='tuesday' or day !='wednesday' or day !='thursday' or day !='friday'):
        day=input('Please enter the week day')
        day=day.lower()
        if(day =='all' or day =='sunday' or day =='monday' or day =='tuesday' or day =='wednesday' or day =='thursday' or day =='friday'):
                print('Cool')
                break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #Load data
    data = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    data['Start Time'] = pd.to_datetime(data['Start Time'])

    # extract month and day of week from Start Time to create new columns
    data['month'] = data['Start Time'].dt.month
    data['day_of_week'] = data['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        data = data[data['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        data = data[data['day_of_week'] == day.title()]



    return data


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""


    # display the most common month if the user didn't filter by a specific month
    if(month=="all"):
        print('Most common month:',df['month'].mode()[0])



    # display the most common day of week if the user filtered by all
    if(day=="all"):
        print('Most common week day:',df['day_of_week'].mode()[0])


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('Most popular hour:',df['hour'].mode()[0])

    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""


    # display most commonly used start station
    print('Most used start station:',df['Start Station'].mode()[0])

    # display most commonly used end station
    print('Most used end station:',df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df2 = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)
    print('Most frequent combination of stations: ', df2.index[0])
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""


    # display total travel time
    print('Total trip duration time: ',df['Trip Duration'].sum())

    # display mean travel time
    print('Average trip duration time: ',df['Trip Duration'].mean())

    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""


    # Display counts of user types
    print('We have: ',df['User Type'].value_counts())


    # Display counts of gender
    if(city!='washington'):
        print('We have: ',df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    if(city!='washington'):
        print('Earliest year of birth: ',df['Birth Year'].min())
        print('Most recent year of birth: ',df['Birth Year'].max())
        print('Most common year of birth: ',df['Birth Year'].mode()[0])

    print('-'*40)
    question=input('this set has %d rows.\nWould you like to see the raw data?\nYes or no' %(df.shape[0]))
    if(question.lower()=='yes'):
            maxrow=4
            for i in range (0, df.shape[0], maxrow):
                print(df.iloc[i:maxrow])
                maxrow+=5
                question=input('Would you like to continue vewing the data?\nyes or no')
                if(question.lower()!='yes'):
                    break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
