import re   # helps to gave special charaters
#password length min 8,char,caps,upper,digit,special char

def check_len_pass(password):
    if len(password)<8:
        return f"passoword : {password}  \nWEAK :MIN 8 Len"
    if not any(char.isdigit() for char in password):
        return "WEAK: no Digit have"
    if not any(char.isupper() for char in password):
        return "WEAK: no Upper have"
    if not any(char.islower() for char in password):
        return "WEAK: no Lower have"
    if not re.search(r'[!@#$^*]' , password):
        return "Required special_character"
    return "STRONG: Password is secured!!"
while True:
    password=input("Enter Password : ")
    if password=="exit":
        print("EXIT")
        break
    result=check_len_pass(password)
    print(result)
    

if __name__ == "__main__":
    check_len_pass(password)