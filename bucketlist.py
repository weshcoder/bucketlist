bucket_list = []


def show_help():
  print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to show bucket_list
Enter 'DELETE' to delete your hole bucketlist""")
  
  
def add_to_list(item):
  bucket_list.append(item)
  print("Added! Your Bucketlist has {} items.".format(len(bucket_list)))
  
def show_list():
  print("Here's your bucketlist:")
  for item in bucket_list:
    print(item)
  if 

def delete_list():
  remove = input("Do you want to delete the list? (YES/NO)")
  if remove == "yes":
    del bucket_list[:]
    print("Your bucketlist has been deleted")
  
show_help()
  
while True:
    new_item = input("Add Bucketlist -> ")
    
    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue
    elif new_item == "DELETE":
        delete_list()
        continue
    add_to_list(new_item)

show_list()
