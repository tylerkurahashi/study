# 4-1
guess_me = 7
if guess_me == 7:
    print('Just right')
elif guess_me < 7:
    print('Too low')
else:
    print('Too high')

# 4-2
guess_me = 7
start = 6
while guess_me >= start:
    if guess_me == start:
        print("found it!")
        break
    elif guess_me < start:
        print("oops!")
        break
    else:
        print("Too low")

    start += 1

# 4-3
numbers = [3,2,1,0]
for num in numbers:
    print(num)

# 4-4
evens = [num for num in range(10) if num%2 == 0]
print(evens)

# 4-5
squares = {num: num**2 for num in range(10)}
print(squares)

# 4-6
odd_set = {num for num in range(10) if num % 2 == 1}
print(odd_set)

# 4-7
gen = (f"Got {num}" for num in range(10))
print(gen)
for out in gen:
    print(out)

# since data in the generator is consumed, output is none
print("2nd")
for out in gen:
    print(out)

# 4-8
def good():
    return ['Harry','Ron','Harmione']

print(good())

# 4-9
def get_odds():
    for num in range(10):
        if num % 2 == 1:
            yield num

odds = [num for num in get_odds()]
print(odds[3])

# 4-10
def decorator(func):
    def new_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func

@decorator
def add(a,b):
    print(a+b)
    return a+b

add(1,2)

# 4-11
class OopsException(Exception):
    pass

word = "haha"
# raise OopsException(word)

# 4-12
titles = ['Creature of Habit', 'Crewl Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
result = list(zip(titles, plots))
dictionary = {}
for key, value in result:
    dictionary[key] = value

print(dictionary)