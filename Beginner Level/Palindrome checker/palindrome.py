#* palindrome checker

# এখানে ইউজার থেকে একটি স্ট্রিং শব্দ নেওয়া হচ্ছে
get_user_value = input('Enter your word: ')  

# স্পেস থাকলে প্রথম শব্দ নেয়া

# এখানে পরিক্ষা করা হচ্ছে যে যদি স্ট্রিং একাধিক ওয়ার্ড থাকে তাহলে
if ' ' in get_user_value:
    # প্রথম স্পেস থেকে বাকি টেক্সট গুলো কেটে শুধুমাত্র প্রথম শব্দ নিবে
    new_user_value = get_user_value[0:get_user_value.index(' ')]  
else:
    # আর যদি স্পেস অর্থাৎ একাধিক শব্দ না থাকে তাহলে স্ট্রিং যেটা থাকবে সেটাই কাউন্ট হবে 
    new_user_value = get_user_value   
        

#  এখানে বিগিনার হিসেবে সঠিকভাবে কোডগুলো বোঝার জন্য নিচে লাইন বাই লাইন কোড করা হয়েছে, কারণ ফাংশন ব্যবহার করে
#  এই লাইন গুলোকে আরো ছোট এবং সহজ করা যাবে। নিচের লাইন গুলো ব্যবহার করার কারণ হচ্ছে
#  স্ট্রিং মেথড গুলোর সঠিক ব্যবহার শেখার জন্য   

# প্যালিন্ড্রোম পরিক্ষা চালানোর জন্য শব্দটিকে প্রস্তুত করা হচ্ছে

# এখানে ইউজারের দেয়া শব্দটিকে লিস্টে রুপান্তর করা হচ্ছে। যেমনঃ '' ~ []     
value_splite = list(new_user_value)
# এখানে লিস্টটিকে শেষ থেকে শুরু করার জন্য রিভার্স মেথড ব্যবহার করা হয়েছে
value_splite.reverse()
# এখানে রিভার্স লিস্টটিকে জয়েন মেথড এর মাধ্যমে একটি শব্দে রুপান্তর করা হচ্ছে। 
join_value = ''.join(value_splite)


# প্যালিনড্রোম যাচাই

# যদি ইউজার ইনপুটে কোনো প্রকার ভ্যালু না দিয়ে থাকে অর্থাৎ ইনপুট যদি খালি থাকে তাহলে 'Enter a valid word' প্রিন্ট হবে
if new_user_value == '' :
    print('Enter a valid word')
# যদি ইউজারের দেওয়া শব্দটি প্যালিন্ড্রোম যাচাইয়ে সঠিক হয় তাহলে 'Your word is palindrome' এটা প্রিন্ট হবে
elif new_user_value == join_value:
    print('Your word is palindrome')
# যদি ইউজারের দেওয়া শব্দটি প্যালিন্ড্রোম যাচাইয়ে ব্যার্থ তাহলে 'Your word is not palindrome' এটা প্রিন্ট হবে
else:
    print('Your word is not palindrome')