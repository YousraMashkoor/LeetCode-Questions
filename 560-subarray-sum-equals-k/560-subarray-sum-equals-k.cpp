// Commulative Sum

/*

[1,1,1] 2


*/

#include <iostream>
using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        
        int sum = 0;
        int count = 0;
        
        unordered_map<int,int> seen = {{0,1}};
        
        for(int n: nums){
            sum +=n;
            count += seen[sum-k];
            seen[sum]++;
        }
        
        return count;
        
    }
};