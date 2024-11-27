from enum import Enum

## some user use enums for creating constans, because there is no CONSTANTS in Python
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1


print(State(1))
print(State(0))

print(State['ACTIVE'])
print(State['ACTIVE'].value)

print(list(State))
