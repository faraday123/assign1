import random

""""
Question 1
"""

def fib(end):
    new_number = 1
    counter = 0
    while counter < end:
        print(counter)
        previous = new_number
        new_number = counter
        counter = previous + new_number


fib(10)

"""
Question 2
"""


def guessingGame(start=1, end=9):
    random_number = random.randint(1, 9)
    counter = 0
    con = True
    while con:
        number = int(input("Guess the number: "))
        counter = counter + 1
        if number < random_number:
            print("You guessed very low")

        elif number is random_number:
            print("You guessed the exact number")
            con = False
        else:
            print("You guessed very high")
    print("Number of tries:", counter)


guessingGame()


"""
Question 3
"""


def add_tags(tag=None, text=None):
    tag1 = "<"
    tag2 = ">"
    tag3 = "/>"
    open_tag = tag1 + tag + tag2
    close_tag = tag1 + tag + tag3
    print("\'"+open_tag + text + close_tag+"\'")


add_tags("h2", "This string can be as long as you want it to be")


"""
Question 4
"""

sample_text = """
President Akufo-Addo has through the Interior Ministry announced Monday,March 8 as a public holiday.
This, according to a statement on the ministry’s website on March 1, is
because the country’s Independence Day which is a Statutory Public Holiday
falls on a weekend.
“The general public is hereby notified that Saturday, 6th March, 2021 marks
Independence Day which is a Statutory Public Holiday.
“However, in view of the fact that 6th March, 2021 falls on a Saturday, His
Excellency, the President of the Republic of Ghana, has by Executive
Instrument (E.I), in accordance with section 2 of the Public Holidays and
Commemorative Days Act, 2001 (Act 601) declared Monday, 8th March, 2021 as a
Public Holiday and should be observed as such throughout the country.”
The release was signed by the Interior Minister-designate, Ambrose Dery.
source::https://www.myjoyonline.com/akufo-addo-declares-march-8-publicholiday/
"""


def hyperlink(href, text):
    """
    Takes a url and display text and returns and html anchor
    """

    para1 = text.find("President")
    end = text.find(".")
    p1 = text[para1:end + 1]
    print("<h2>" + p1 + "</h2>")
    print("<p></p>")
    # second paragraph
    para2 = text.find("This")
    end = text.find(".", para2)
    p2 = text[para2:end + 1]
    print("<p>" + p2 + "</p>")
    print("<p></p>")
    # third paragraph
    para3 = text.find("The")
    end = text.find(".", para3)
    p3 = text[para3:end + 1]
    print("<p>" + p3 + "</p>")
    print("<p></p>")

    # fourth paragraph
    para4 = text.find("However", end)
    end1 = text.find("country", end + 1)
    p4 = text[para4 - 1:end1 + 9]
    print("<p>" + p4 + "</p>")
    print("<p></p>")

    # fifth paragraph
    para5 = text.find("The", end1)
    end = text.find(".", para5)
    p5 = text[para5:end]
    print("<p>" + p5 + "</p>")
    print("<p></p>")
    # last paragraph

    last_para = text.find("https")
    end = text.find("holiday", last_para)
    lp = text[last_para:end + 1]
    last_para_source = text.find("source")
    lps = text[last_para_source:-73]
    print("<a href =" + lp + ">" + lps + "</p>")

    return "<a href={""}>{""}</a>".format(href, text)


hyperlink("https://www.myjoyonline.com/akufo-addo-declares-march-8-publich", sample_text)
