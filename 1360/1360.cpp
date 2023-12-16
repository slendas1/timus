#include <iostream>
#include <math.h>

using namespace std;

int main(){
    double x, y;
    double eps;
    double pi = atan(1) * 4;
    cin >> x >> y;
    cin >> eps;
    double t = acos(y);
    // cout << t << endl;
    while (abs(x - sin(sqrt(t))) >  eps){
        t += 2 * pi;
    }
    cout.precision(8);
    cout.setf(ios::fixed);

    cout << t << "\n";
    return 0;
}