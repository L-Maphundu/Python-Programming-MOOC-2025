# Write your solution here
def inscription():
    sign_to = input("Whom should I sign this to: ").strip()
    save_location = input("Where shall I save it: ").strip()

    with open(save_location, "w") as writing:
        writing.write(f'Hi {sign_to}, we hope you enjoy learning Python with us! Best, Mooc.fi Team')

inscription()