def myfunc(n):
  return len(n)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
##[4,10,3,2]
cars.sort(reverse=True)
print(cars)
x = map(lambda n:len(n), ('Ford', 'Mitsubishi', 'BMW', 'VW'))
print(list(x))

