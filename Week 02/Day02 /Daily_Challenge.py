print("\n--- Daily Challenge: Pagination ---\n")

"""
Daily Challenge : Pagination
Last Updated: September 22nd, 2023

What You Will Learn :
OOP

Instructions :
Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

The Pagination class will accept 2 parameters:

items (default: None): It will contain a list of contents to paginate.
pageSize (default: 10): The amount of items to show in each page.
So for example we could initialize our pagination like this:

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)

The Pagination class will have a few methods:

getVisibleItems() : returns a list of items visible depending on the pageSize
So for example we could use this method like this:

p.getVisibleItems() 
# ["a", "b", "c", "d"]
You will have to implement various methods to go through the pages such as:
prevPage()
nextPage()
firstPage()
lastPage()
goToPage(pageNum)

Here’s a continuation of the example above using nextPage and lastPage:

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)

p.getVisibleItems() 
# ["a", "b", "c", "d"]

p.nextPage()

p.getVisibleItems()
# ["e", "f", "g", "h"]

p.lastPage()

p.getVisibleItems()
# ["y", "z"]

Notes

The second argument (pageSize) could be a float, in that case just convert it to an int (this is also the case for the goToPage method)
The methods used to change page should be chainable, so you can call them one after the other like this: p.nextPage().nextPage()
Please set the p.totalPages and p.currentPage attributes to the appropriate number as there cannot be a page 0.
If a page is outside of the totalPages attribute, then the goToPage method should go to the closest page to the number provided (e.g. there are only 5 total pages, but p.goToPage(10) is given: the p.currentPage should be set to 5; if 0 or a negative number is given, p.currentPage should be set to 1).
"""

from typing import Self
# Item 1
class Pagination():


# Item 2
    def __init__(self, items = None , pageSize = 10) -> None:
        self.items = items
        self.pageSize = int(pageSize)
        self.value = 1



# Item 3
    def getVisibleItems(self):
        visible = []
        if self.value * self.pageSize > len(self.items):
            limit = len(self.items)
        else:
            limit = self.pageSize * self.value
        for i in range((self.value-1) * self.pageSize, limit):
                visible.append(self.items[i])
        print(visible)


    def prevPage(self) -> Self:
        if self.value == 0:
            pass
        else:
            self.value -= 1
        return self

    def nextPage(self) -> Self:
        if self.value == self.totalPages():
            pass
        else:
            self.value += 1
        return self

    def firstPage(self) -> Self:
        self.value = 0
        return self

    def lastPage(self) -> Self:
        self.value = self.totalPages()
         return self

    def goToPage(self, pageNum) -> Self:
        self.pageNum = pageNum
        if pageNum > self.totalPages():
            set.value = self.totalPages()
        elif pageNum < 1:
            set.value = 1
        else:
            set.value = int(pageNum)
        return self

    def totalPages(self):

        if len(self.items) % self.pageSize == 0 :
            return int ( len(self.items) / self.pageSize )
        else:
            return int ( len(self.items) / self.pageSize ) + 1




alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)

p.getVisibleItems()

p.nextPage()

p.getVisibleItems()

p.lastPage()

p.getVisibleItems()

p.nextPage().nextPage()

