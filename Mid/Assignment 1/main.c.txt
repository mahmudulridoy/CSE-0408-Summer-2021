#include<bits/stdc++.h>
using namespace std;
#define D(x) cerr<<__LINE__<<" : "<<#x<<" -> "<<x<<endl
#define rep(i,j) for(int i = 0; i < 3; i++) for(int j = 0; j < 3; j++)
#define PII pair < int, int >
typedef vector<vector<int>> vec2D;

const int MAX = 1e5+7;
int t=1, n, m, l, k, tc;

int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

vec2D init{
    {8, 1, 2},
    {3, 6, 4},
    {0, 7, 5}
};
vec2D goal{
    {1, 3, 2},
    {8, 0, 4},
    {7, 6, 5}
};
/// using a structure to store information of each state
struct Box {
    vec2D mat{ { 0,0,0 },{ 0,0,0},{ 0,0,0} };
    int diff, level;
    int x, y;
    int lastx, lasty;
    Box(vec2D a,int b = 0, int c = 0, PII p = {0,0}, PII q = {0,0}) {
        rep(i,j) mat[i][j] = a[i][j];
        diff = b;
        level = c;
        x = p.first;
        y = p.second;
        lastx = q.first;
        lasty = q.second;
    }
};

/// operator overload for which bases priority queue work
bool operator < (Box A, Box B) {
    if(A.diff == B.diff) return A.level < B.level;
    return A.diff < B.diff;
}

/// heuristic function to calculate mismatch position
int heuristic_function(vec2D a, vec2D b) {
    int ret(0);
    rep(i,j) if (a[i][j] != b[i][j]) ret--;
    return ret;
}

/// checking puzzle boudaries
bool check(int i, int j) {
    return i>=0 and i<3 and j>=0 and j<3;
}

/// this function used to show state status
void print(Box a) {
    rep(i,j)
    cout << a.mat[i][j] << (j == 2 ? "\n" : " ");
    cout << " heuristic Value is :  " << -a.diff << "\n";
    cout << " Current level is : " << -a.level << "\n\n";
}

/// used to get new state which can be jump from current state
Box get_new_state(Box now, int xx, int yy) {
    Box temp = now;
    swap(temp.mat[temp.x][temp.y], temp.mat[xx][yy]);
    temp.diff = heuristic_function(temp.mat, goal);
    temp.level = now.level - 1;
    temp.x = xx;
    temp.y = yy;
    temp.lastx = now.x;
    temp.lasty = now.y;
    return temp;
}


/// this is modified version of dijkstra shortest path algorithms
/// basically work on those state first which heuristic value lesser
void dijkstra(int x, int y) {
    map < vec2D,  bool > mp;
    priority_queue < Box > PQ;
    int nD = heuristic_function(init, goal);
    Box src = {init, nD, 0, {x,y}, {-1,-1}};
    PQ.push(src);
    int state = 0;
    while(!PQ.empty()) {
        state++;
        Box now = PQ.top();
        PQ.pop();
        cout << "Step no : " << state-1 <<"\n";
        print(now);
        if(!now.diff) { /// if heuristic value is zero it means we are on goal
            puts("Goal state has been discovered");
            cout << "level : " << -now.level << "\n";
            cout << " Step no : " << state-1 <<"\n";
            break;
        }
        if(mp[now.mat]) continue;
        mp[now.mat] = true;
        for(int i = 0; i < 4; i++) {
            int xx = now.x + dx[i];
            int yy = now.y + dy[i];
            if(check(xx, yy)) {
                if(now.lastx == xx and now.lasty == yy) continue;
                Box temp = get_new_state(now, xx, yy);
                PQ.push(temp);
            }
        }
    }
}

signed main() {
    puts("Current State:");
    rep(i,j) cout << init[i][j] << (j == 2 ? "\n" : " ");
    puts("");
    puts("Goal State:");
    rep(i,j) cout << goal[i][j] << (j == 2 ? "\n" : " ");
    puts("\n............Search Started...............\n");
    rep(i,j) if(!init[i][j]) dijkstra(i,j); /// this will find zero-th position and start
    return 0;
}
