class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length()!=t.length())
         return false;

        unordered_map<char,int> charCount;

        for(char ch:s){
            charCount[ch] +=1;
        }

        for(char ch:t){
            charCount[ch] -=1;
        }

        for(auto it:charCount){
            if(it.second!=0){
                return false;
            }
        }
        return true;
    }
};
