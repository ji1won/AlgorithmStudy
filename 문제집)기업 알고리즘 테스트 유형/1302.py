total = int(input())
book = {}

for i in range(total):
    title = input()
    if title in book:
        book[title] += 1
    else:
        book[title] = 1

max_count = max(book.values())
best_books = [title for title, count in book.items() if count == max_count]
best_books.sort()

print(best_books[0])
