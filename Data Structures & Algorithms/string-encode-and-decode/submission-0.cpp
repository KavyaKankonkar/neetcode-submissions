class Solution {
public:

    string encode(vector<string>& strs) {
     string res="";

     for(auto &s:strs){
        for(auto &c:s){
            res.push_back(c);
        }
        res.push_back('/');
     }
     return res;
    }

    vector<string> decode(string s) {
    vector<string> res;
    string curr="";

    for(auto it: s){
    if(it=='/'){
        res.push_back(curr);
        curr="";
    }
    else{
     curr.push_back(it);
    }
    }
    return res;
    }
};
