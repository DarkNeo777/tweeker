import tweepy
client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAAKtmkgEAAAAAusOc1vGWdEkty7wWwb%2B38ptDyJ8%3DVZbI8u3nuz1pAod4YwyzEK4F2LVt0UgpWvtXuBlaM8rYe0Bjnb")

people = {
    'elon musk' : 'elonmusk',
    'Joe Rogan' : 'joerogan',
    'Lex Fridman': 'lexfridman',
    'Andrew Huberman': 'hubermanlab',
    'David Goggins': 'davidgoggins'
}

search1 = ''
choice = ''

def radio_entered():
    if(search1[:1] == '@'):
        search1 = search1[1:]

    if(search1 == 'people'): 
        while(search1 != choice):
            temp = 0
            x = people.keys()
            print(x)
            choice = input('Enter name from index: ')
            for i in people:
                if(choice == i):
                    temp = 0
                    search1 = people[i]
                    choice = search1
                    break
                else: temp = 1
                if(temp == 1):
                    print("Enter a valid person")


def user_entered(user_name):

    #print("Twitter handle is: " + search1)
    information = client.get_user(username=user_name)

    #print(information) #prints the raw response information
    about = information[0]

    id_person = about.get('id')
    more_info = client.get_users_tweets(id_person, exclude='replies')
    '''
    for i,j in about.items():
        print(i,":",j)
        print("")
    '''
    print(about.items())
    
    print("Their most recent tweets: ")
    more_info = more_info[0]
    temp = 1
    for twt in more_info:
        print(temp,"",twt)
        print("")
        temp = temp + 1



