from main import Add

def TestAdd():
    assert Add(2,3) == 5
    assert Add(4,5) == 9
    assert Add(6,7) == 13
    print("Add Function Works")

if __name__ == '__main__':
    TestAdd()