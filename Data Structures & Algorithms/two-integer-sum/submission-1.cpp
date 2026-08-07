class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
       unordered_map<int,int> s;
       vector<int> res;
       for(int i=0;i<nums.size();i++){
        int complement=target-nums[i];

        if(s.find(complement)!=s.end()){
            if(i<s[complement]){
            res.push_back(i);
            res.push_back(s[complement]);
            }
            else{
            res.push_back(s[complement]);
            res.push_back(i); 
            }
        }
        else{
            s[nums[i]]=i;
        }
       }
       return res;
    }
};
