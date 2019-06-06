#include <iostream>
#include <string>
using namespace std;


class door
{
protected:
  int a;
public:
  void print()
  {
    cout << "door" << endl;
  }
};

class bottle_door :public door
{
private:
  int b;
public:
  void print()
  {
    cout << "bottle_door" << endl;
  }
};

int main()
{
  bottle_door x;
  x.print();
  return 0;
}
