def denklem(x):
    return x * (1 - x*2)*0.5 - 1

def find_solution(start, end, step, epsilon):
    x = start
    while x <= end:
        if abs(denklem(x)) < epsilon:
            return x
        x += step
    return None

# [1.0, √(3)] aralığında həll tapmaq üçün
baslanğıc = 1.0
son = (3 ** 0.5)
addım = 0.001
həssaslıq = 1e-6

nəticə = find_solution(baslanğıc, son, addım, həssaslıq)

if nəticə is not None:
    print(f": {nəticə}")
else:
    print("Göstərilən aralıqda heç bir həll tapılmadı")
