class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> s;
        vector<vector<string>> res;
        for(int i=0;i<strs.size();i++){
            string org=strs[i];
            sort(strs[i].begin(),strs[i].end());
            s[strs[i]].push_back(org);
        }
        
        for(auto it:s){
            res.push_back(it.second);
        }

        return res;
    }
};
