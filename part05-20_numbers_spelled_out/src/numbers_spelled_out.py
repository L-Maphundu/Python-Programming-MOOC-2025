# Write your solution here
def dict_of_numbers():
    bases = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'} 
    tens = {10:'ten', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}
    teens = {11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
    
    numbers = {}
    for i in range(0, 100):
        if i < 10:
            numbers[i] = bases[i]
        elif i % 10 == 0:
            numbers[i] = tens[i]
        elif 11 <= i <= 19:
            numbers[i] = teens[i]

        else:
            number = str(i)
            ten = int(number[0] + "0")
            base = int(number[1])

            number2 = tens[ten] + "-" + bases[base]
            numbers[i] = number2


    return numbers

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])