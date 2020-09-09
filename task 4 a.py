student_count = int(input(" How msny students are there? "))
book_count = int(input(" How many books are there? "))
recieve = round(book_count/student_count)
remain = book_count%student_count
print("Students will receive " , recieve, "books and " ,remain, "books remain")
                    
