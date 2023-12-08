#include <iostream>
#include <vector>
#include <utility>
#include <algorithm> 

using namespace std;

int gcd(int a, int b){
    if(a < b){
        int r = a;
        a = b;
        b = r;
    }
    if(b == 0){
        return a;
    }
    return gcd(b, a % b);
}

int main(){
    int n;
    cin >> n;
    vector<pair<int, int> > v;
    for(int i = 0; i < n; i++){
        int a;
        cin >> a;
        v.push_back(make_pair(a, i));
    }
    sort(v.begin(), v.end());

    int res = 0;
    int res1 = 0;
    for(int i = 0; i < n; i++){
        res = gcd(abs(v[i].second - i), res);
        res1 = gcd(abs((n - 1 - v[i].second) - i), res1);
    }

    if(min(res, res1) == 0){
        cout << n - 1 << endl;
    } else{
        cout << max(res, res1) - 1 << endl;
    }
    return 0;
}