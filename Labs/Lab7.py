import wikipedia
print( wikipedia.summary("San Francisco 49ers"))
#This just prints the summary of a specific wikipedia page. In this instance the NFL team 49ers.
search = wikipedia.search("Toy Story")
print(search)
#This is a search done through the plugin showing what articles are available for that search word or words.
print(wikipedia.random(pages=5))
#This returns 5 random wikipedia web pages.
