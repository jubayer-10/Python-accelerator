get_user_value = input('Enter your Number: ')  # এখানে ইউজার থেকে ইনপুটের মাধ্যমে একটি ভ্যালু নেওয়া হচ্ছে

try:  # যদি ভ্যালু সঠিক হয় অর্থাৎ এমন একটা ভ্যালু যেটাকে নাম্বারে কনভার্ট করা যাবে। ভ্যালু সঠিক হলে নিচের পরীক্ষা গুলো কাজ করবে
    
    convert_number = float(get_user_value)  # ভ্যালুকে স্ট্রিং থেকে নাম্বারে কনভার্ট করা হচ্ছে

    if convert_number % 3 == 0 and convert_number % 5 == 0:   # এখানে পরীক্ষা করা হচ্ছে, যদি ভ্যালুকে ৩ এবং ৫ দিয়ে ভাগ করা যায় তাহলে 
        print('Your number is FizzBuzz')  # এটা প্রিন্ট হবে
    elif convert_number % 3 == 0:   # এখানে পরীক্ষা করা হচ্ছে, যদি ভ্যালুকে শুধুমাত্র ৩ দিয়ে ভাগ করা যায় তাহলে 
        print('Your number is Fizz')  # এটা প্রিন্ট হবে
    elif convert_number % 5 == 0:   # এখানে পরীক্ষা করা হচ্ছে, যদি ভ্যালুকে শুধুমাত্র ৫ দিয়ে ভাগ করা যায় তাহলে 
        print('Your number is Buzz')  # এটা প্রিন্ট হবে
    else:
        print(f'Your number is {convert_number}')   # আর যদি ৩ অথবা ৫ একটা দিয়েও ভাগ করা না যায় তাহলে এটা প্রিন্ট হবে

except ValueError: # এখানে যদি ভ্যালু ইলেগেল হয়, যেমন "myNAme", "demo", "example" হয় তাহলে নিচের ভ্যালু প্রিন্ট হবে
        print('Please enter a valid number')