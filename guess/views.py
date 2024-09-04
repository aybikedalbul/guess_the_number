from django.shortcuts import render
import random

def guess(request):
    feedback = ""

    if request.method == 'POST':
        try:
            user_guess = int(request.POST.get('userGuess', 0))
        except ValueError:
            feedback = 'Please enter a vsalid number'
            return render(request, 'guess/index.html', {'feedback': feedback})
        
        random_number = random.randint(1,10)

        if user_guess < random_number:
            feedback = 'Sorry, guess again. Too low.'
        elif user_guess > random_number:
            feedback = 'Sorry, guess again. Too high.'
        else:
            feedback = f'Yaay, congrats! you have guessed the number {random_number}'
    
    return render(request, 'guess/index.html', {'feedback': feedback})



def homepage(request):
    return render(request, 'guess/homepage.html')