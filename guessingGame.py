#game
secret_word = "pommy"
guess = ""
count = 0
limit= 3
out_of_g = False
while guess!= secret_word and not(out_of_g):
    if count < limit:
      guess = input("Enter guess: ")
      count+=1
    else:
        out_of_g = True
if out_of_g:
    print("LOSERRR")
else:
    print("You got it!")