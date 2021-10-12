def password_check(str1):
      
    SpecialSym =['$', '@', '#', '%']
    val = True
    sub='abc'
    sub1='qwerty'
      
    if len(str1) < 8:
        print('length should be at least 8')
        val = False
          
    if not any(char.isdigit() for char in str1):
        print('String should have at least one numeral')
        val = False
          
    if not any(char.isupper() for char in str1):
        print('string should have at least one uppercase letter')
        val = False
          
    if not any(char in SpecialSym for char in str1):
        print('String should have at least one of the symbols $@#')
        val = False
    if sub in str1:
        print("it contain abc")
        val= False
    
    if sub1 in str1:
        print("contain Qwerty")
        val=False

    if val:
        return val
  
def main():
    str1 = 'W$fskdjfs@@4429'
      
    if (password_check(str1)):
        print("String is valid")
    else:
        print("String is invalid !!")
               
if __name__ == '__main__':
    main()