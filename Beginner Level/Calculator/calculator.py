def addition(x, y):   # এখানে এমন একটি ফাংশন তৈরি করা হয়েছে যেখানে ইউজারের দেওয়া দুইটা ভ্যালুর যোগফল(addition) নির্ণয় করবে
    return x + y

def subtarction(x, y):   # এখানে এমন একটি ফাংশন তৈরি করা হয়েছে যেখানে ইউজারের দেওয়া দুইটা ভ্যালুর বিয়োগফল(subtarction) নির্ণয় করবে
    return x - y

def multiplication(x, y):   # এখানে এমন একটি ফাংশন তৈরি করা হয়েছে যেখানে ইউজারের দেওয়া দুইটা ভ্যালুর ্গুণফল(multiplication) নির্ণয় করবে
    return x * y

def divide(x, y):       # এখানে এমন একটি ফাংশন তৈরি করা হয়েছে যেখানে ইউজারের দেওয়া দুইটা ভ্যালুর ্ভাগফল(divide) নির্ণয় করবে
    if y != 0:          # এখানে একটা কন্ডিশন দেওয়া হয়েছে যে, y এর মান শুন্য না হলে ভাগফল বের করবে, আর y এর মান শুন্য হলে ইরোর আসবে। কারণ y এর মান শূন্য হলে ভাগফল বের করা সম্ভব না।
        return x / y
    else:
        return print('Please enter valid number')
    
    
def calculator():
    
    fristNumber = float(input('Enter your frist number: '))   # ইউজার থেকে প্রথম ভ্যালু নেওয়ার ইনপুট
    lastNumber = float(input('Enter your last number: '))   # ইউজার থেকে দ্বিতীয় ভ্যালু নেওয়ার ইনপুট

    get_user_oparation = input('Which oparation you want? (+, -, *, /): ')   # ইউজার কি রকম অপারেশন চাচ্ছে সেটা নির্ধারণের জন্য ইনপুট টাইপ

    if get_user_oparation == '+':    # যদি ইউজার দেওয়া ইনপুট ভ্যালু (+) হয় তাহলে নিচের আউটপুট প্রিন্ট করবে
        print(f'Total addition {fristNumber} + {lastNumber} = {addition(fristNumber, lastNumber)}')  # এখানে f_string এর মাধ্যমে স্ট্রিং এবং ভেরিএইবল যোগ করা হয়েছে এবং addition ফাংশনে ভ্যালু পাস করা হচ্ছে
    elif get_user_oparation == '-':    # যদি ইউজার দেওয়া ইনপুট ভ্যালু (-) হয় তাহলে নিচের আউটপুট প্রিন্ট করবে
        print(f'Total subtraction {fristNumber} - {lastNumber} = {subtarction(fristNumber, lastNumber)}')  # এখানে f_string এর মাধ্যমে স্ট্রিং এবং ভেরিএইবল যোগ করা হয়েছে এবং subtarction ফাংশনে ভ্যালু পাস করা হচ্ছে
    elif get_user_oparation == '*':    # যদি ইউজার দেওয়া ইনপুট ভ্যালু (*) হয় তাহলে নিচের আউটপুট প্রিন্ট করবে
        print(f'Total multiplication {fristNumber} * {lastNumber} = {multiplication(fristNumber, lastNumber)}')  # এখানে f_string এর মাধ্যমে স্ট্রিং এবং ভেরিএইবল যোগ করা হয়েছে এবং multiplication ফাংশনে ভ্যালু পাস করা হচ্ছে
    elif get_user_oparation == '/':    # যদি ইউজার দেওয়া ইনপুট ভ্যালু (/) হয় তাহলে নিচের আউটপুট প্রিন্ট করবে
        print(f'Total divide {fristNumber} * {lastNumber} = {divide(fristNumber, lastNumber)}')  # এখানে f_string এর মাধ্যমে স্ট্রিং এবং ভেরিএইবল যোগ করা হয়েছে এবং divide ফাংশনে ভ্যালু পাস করা হচ্ছে
    else:
        print('Wrong oparation')   # যদি ইউজারের দেওয়া ভ্যালু (+, -, *, /) এগুলো না হয় তাহলে নিচের আউটপুট প্রিন্ট করবে


calculator()   # পরিশেষে সম্পূর্ণ ক্যাকুলেটরে আউটপুট পাওয়ার জন্য উক্ত ফাইংশনটিকে কল করা হয়েছে