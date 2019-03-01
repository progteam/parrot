"""
backend/scoreboard/kattis_scraping.py

Utility functions for retrieving data from Kattis
"""
import requests
from bs4 import BeautifulSoup


class Error404(Exception):
    """
    Kattis profile with passed user handle does not exist
    """


class ErrorInvalid(Exception):
    """
    Profile with matching user handle is not of CSUMB student
    """


def is_student(soup):
    """
    Checks if user profile is of CSUMB student

    Parameters:
    soup: (BeautifulSoup): Processed profile page

    Returns:
    Bool: Returns True if CSUMB student, else False
    """
    return soup.find(class_="university-logo").find_all(
        'a', href=True
    )[1].text == "California State University, Monterey Bay"


def get_score(user_handle, check_school=False):
    """
    Retrieves score from user page

    Parameters:
    user_handle (str): Formatted kattis username for profile page
    check_school (bool): If it is set to true, we will throw an ErrorInvalid if
        the user is not listed under CSUMB on Kattis.

    Returns:
    float: If valid name, returns score of user
    """
    try:
        page = requests.get(f"https://open.kattis.com/users/{user_handle}")
        soup = BeautifulSoup(page.content, 'html.parser')
        score = float(str(soup.find(class_="rank clearfix").text).split()[2])

        if check_school and not is_student(soup):
            raise ErrorInvalid(
                f"{user_handle} does not appear to be a CSUMB student"
            )
        return score
    except AttributeError:
        raise Error404(f"Cannot load the profile for {user_handle}")


def get_rank(user_handle, check_school=False):
    """
    Retrieves rank from user page

    Parameters:
    user_handle (str): Formatted kattis username for profile page
    check_school (bool): If it is set to true, we will throw an ErrorInvalid if
        the user is not listed under CSUMB on Kattis.

    Returns:
    int: If valid name, returns rank of user
    """
    try:
        page = requests.get(f"https://open.kattis.com/users/{user_handle}")
        soup = BeautifulSoup(page.content, 'html.parser')
        rank = int(str(soup.find(class_="rank clearfix").text).split()[1])

        if check_school and not is_student(soup):
            raise ErrorInvalid(
                f"{user_handle} does not appear to be a CSUMB student"
            )
        return rank
    except AttributeError:
        raise Error404(f"Cannot load the profile for {user_handle}")
