class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<vector<int>> bucket(nums.size()+1);
         unordered_map<int,int> hm;
         vector<int> res;
      
        for(int n:nums){
                hm[n]++;
        }

        for(auto& [num,freq]:hm){
            bucket[freq].push_back(num);
        }
        
        for(int j=nums.size();j>=0 && k>0;--j){
           for(int n: bucket[j]){
              res.push_back(n);
              k--;
            if (k<0){
                break;
            }
            }

        }
        return res;
    }
};
