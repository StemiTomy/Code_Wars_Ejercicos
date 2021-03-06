"""8 kyu Beginner Series #1 School Paperwork
Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

Example:
n= 5, m=5: 25
n=-5, m=5:  0
"""
def paperwork(n, m):
    """Paperwork function

    Args:
        n (int): number of roomates
        m (int): number of paper work

    Returns:
        int: total copies needed to copy
    """
    if n < 0 or m < 0:
        return 0
    return n*m

# mejor solucion
def paperwork2(n, m):
    return n * m if n > 0 and m > 0 else 0
