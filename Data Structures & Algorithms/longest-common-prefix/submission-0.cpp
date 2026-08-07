class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        sort(strs.begin(),strs.end());
        int c=0;
        int mini=INT_MAX;
        if(strs[0][0]!=strs[strs.size()-1][0]){
            return "";
        }
        for(int i=0;i<strs.size();i++){
            int len=strs[i].size();
          mini=min(mini,len);
        }
        for(int i=0;i<mini;i++){
            
            if(strs[0][i]==strs[strs.size()-1][i]){
                c++;
            }
        }
        if(c==0){
            return "";
        }
        else{
            return strs[0].substr(0,c);
        }
    }
};