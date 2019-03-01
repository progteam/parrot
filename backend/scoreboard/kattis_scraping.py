import requests
from bs4 import BeautifulSoup


class Error(Exception):
    pass


class Error404(Error):
    """
    Kattis profile with passed user handle does not exist

    """
    pass


class ErrorInvalid(Error):
    """
    Profile with matching user handle is not of CSUMB student

    """
    pass


def is_student(soup):
    """
    Checks if user profile is of CSUMB student

    Parameters:
    soup: (BeautifulSoup): Processed profile page

    Returns:
    Bool: Returns True if CSUMB student, else False

    """

    school = soup.find_all('a', href=True)[13].text

    return school == "California State University, Monterey Bay"


def get_points(user_handle):
    """
    Retrieves points from user page

    Parameters:
    user_handle (str): Formatted kattis username for profile page

    Returns:
    float: If valid name, returns score of user

    """

    try:
        page = requests.get(f"https://open.kattis.com/users/{user_handle}")
        soup = BeautifulSoup(page.content, 'html.parser')

        score = float(str(soup.find(class_="rank clearfix").text).split()[2])

        if not is_student(soup):
            raise ErrorInvalid

        return score

    except AttributeError:
        raise Error404


def get_rank(user_handle):
    """
    Retrieves rank from user page

    Parameters:
    user_handle (str): Formatted kattis username for profile page

    Returns:
    int: If valid name, returns rank of user

    """

    try:
        page = requests.get(f"https://open.kattis.com/users/{user_handle}")
        soup = BeautifulSoup(page.content, 'html.parser')

        rank = int(str(soup.find(class_="rank clearfix").text).split()[1])

        if not is_student(soup):
            raise ErrorInvalid

        return rank

    except AttributeError:
        raise Error404

