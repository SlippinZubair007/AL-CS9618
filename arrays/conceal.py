
#card=******345
def conceal(cardno):
    x=0
    res=""
    try:
      for word in cardno:
         if (x<len(cardno)-3):
            res+='*'
         else:
            res+=word
         x+=1
      print(f"Concealed card number : {res}\n")
    except Exception as e:
        print(f"Error: {e}")

conceal("zubair123")



