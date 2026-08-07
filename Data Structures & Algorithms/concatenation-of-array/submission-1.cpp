class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n=nums.size();
        vector<int> ans(2*n);
        
        int i=0;
        while(i<n){
            ans[i]=nums[i];
            i++;
        }

        i=0;
        while((i+n)<(2*n)){
         ans[i+n]=nums[i];
         i++;
        } 
        
        return ans;
        }
};