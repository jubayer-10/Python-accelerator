import string  #  import string ব্যবহার করা হয় স্ট্রিং সম্পর্কিত কিছু বিশেষ ফাংশনালিটি এবং কনস্ট্যান্টস ব্যবহার করার জন্য

get_user_password = input('Enter your password: ')   # এখানে ইউজার থেকে পাসওয়ার্ড নেওয়া হচ্ছে

has_alpha = any(letter.isalpha() for letter in get_user_password)  # এখানে ফাংশনের মাধ্যমে চেক করা হচ্ছে ইউজারের দেওয়া পাসওয়ার্ডে একটি হলেও অক্ষর(a-z, A-Z) আছে কিনা

has_number = any(letter.isdigit() for letter in get_user_password)  # এখানে ফাংশনের মাধ্যমে চেক করা হচ্ছে ইউজারের দেওয়া পাসওয়ার্ডে একটি হলেও নাম্বার(0-9) আছে কিনা

has_string = any(letter in string.punctuation for letter in get_user_password)  # এখানে ফাংশনের মাধ্যমে চেক করা হচ্ছে ইউজারের দেওয়া পাসওয়ার্ডে একটি হলেও বিশেষ
                                                                                # ক্যারেক্টার(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~) আছে কিনা আছে কিনা

# কন্ডিশনের মাধ্যমে পরীক্ষা করা হচ্ছে
if has_alpha and has_number and len(get_user_password) >= 8 and has_string:  # পরিশেষে এখানে সব গুলোর সত্যতা যাচাি করা হচ্ছে এবং পাসওয়ার্ড কমপক্ষে ৮ অক্ষরের বেশী হতে হবে এমন শর্ত দেওয়া হয়েছে
    print('Ýour password is strong')  # উপরের সব শর্ত ট্রু(True) রিটার্ন করলে এটা প্রিন্ট হবে
else:
    print('Your password is weak')  # আর উপরের শর্তগুলো মিথ্যা(False) রিটার্ন করলে এটা প্রিন্ট করবে