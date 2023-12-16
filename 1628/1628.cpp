#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int m, n, k;
vector<pair<int, int> > black_days;

bool in_range(pair<int, int> coord){
    return coord.first >= 0 && coord.first < m && coord.second >= 0 && coord.second < n;
}

bool binsearch(pair<int , int> coord){
    int l = 0;
    int r = black_days.size() - 1;

    while (l <= r){
        int m = (r + l) / 2;

        if (black_days[m] == coord){
            return true;
        }

        if (black_days[m] < coord){
            l = m + 1;
        }

        if (black_days[m] > coord){
            r = m - 1;
        }
    }

    return false;
}

bool white_cell(pair<int, int> coord){
    pair<int, int> coord1 = make_pair(coord.first, coord.second);
    pair<int, int> step[] = {make_pair(0, -1), make_pair(0, 1), make_pair(-1, 0), make_pair(1, 0)};
    for (int i = 0; i < 4; i++){
        coord1.first += step[i].first;
        coord1.second += step[i].second;
        if (in_range(coord1) && !binsearch(coord1)){
            return false;
        }
        coord1.first = coord.first;
        coord1.second = coord.second;
    }
    return true;
}

int main(){
    cin >> m >> n >> k;
    
    for(int i = 0; i < m; i++){
        black_days.push_back(make_pair(i, -1));
        black_days.push_back(make_pair(i, n));
    }
    for(int i = 0; i < n; i++){
        black_days.push_back(make_pair(-1, i));
        black_days.push_back(make_pair(m, i));
    }
    for(int i = 0; i < k; i++){
        int x, y;
        cin >> x >> y;
        black_days.push_back(make_pair(x - 1, y - 1));
    }

    sort(black_days.begin(), black_days.end());

    int count = 0;
    
    for(int i = 1; i < black_days.size(); i++){
        if (black_days[i].first == black_days[i - 1].first){
            int white_stripe = black_days[i].second - black_days[i - 1].second - 1;
            if (white_stripe > 1){
                count += 1;
            } else if (white_stripe == 1 && white_cell(make_pair(black_days[i].first, black_days[i].second - 1))){
                count += 1;
            }
        }
    }

    sort(black_days.begin(), black_days.end(), [](pair<int, int> &left, pair<int, int> &right){
        return left.second < right.second || (left.second == right.second && left.first < right.first);
    });

    for(int i = 1; i < black_days.size(); i++){
        if (black_days[i].second == black_days[i - 1].second){
            int white_stripe = black_days[i].first - black_days[i - 1].first - 1;
            if (white_stripe > 1){
                count += 1;
            }
        }
    }

    cout << count << '\n';

    return 0;
}