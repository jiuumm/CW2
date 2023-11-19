#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    vector<int> v;

    for (int i = 0; i < 14; i++) {
        int inp;
        cin >> inp;
        v.push_back(inp);
    }

    int jun = 0, sung = 0;
    int _N = N;
    
    // 준현이의 매수 및 매도 처리를 분리
    for (int i = 0; i < 14; i++) {
        // 준현이의 매수
        if (v[i] <= _N) {
            jun += _N / v[i];
            _N %= v[i];
        }
        // 14일에 매도
        if (i == 13) {
            jun += _N;
        }
    }

    int cnt = 0;
    for (int i = 1; i < v.size(); i++) {
        if (v[i] < v[i - 1]) {
            cnt++;
        } else {
            cnt = 0;
        }
        if (cnt >= 3 && v[i] <= N) {
            // 성민이의 매수
            sung += N / v[i];
            N %= v[i];
            // 3일 연속 하락했을 때의 매수일을 찾으면 종료
            break;
        }
    }

    cnt = 0;
    bool flag = false;
    for (int i = 1; i < v.size(); i++) {
        if (v[i] > v[i - 1]) {
            cnt++;
        } else {
            cnt = 0;
        }
        if (cnt >= 3) {
            // 성민이의 매도
            sung += N;
            flag = true;
            break;
        }
    }

    if (!flag) {
        // 매도를 하지 않았을 경우 14일에 필수로 매도
        sung += N;
    }

    if (sung > jun) {
        cout << "TIMING";
    } else if (sung < jun) {
        cout << "BNP";
    } else {
        cout << "SAMESAME";
    }

    return 0;
}
