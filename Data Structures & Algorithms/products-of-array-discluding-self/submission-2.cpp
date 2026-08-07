class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
     signed int product=1;   
     vector<int> ps(nums.size());
    unordered_map<int,int> count;
    for(int i=0;i<nums.size();i++){
        if(nums[i]==0){
        count[0]+=1;
        }
    }
    if(count[0]>1){
        for(int i=0;i<nums.size();i++){
            ps[i]=0;
        }
        return ps;
    }
    if(find(nums.begin(),nums.end(),0)==nums.end()){
    for(int i=0;i<nums.size();i++){    
     product *=nums[i];
     }

      for(int i=0;i<nums.size();i++){
        ps[i]=(product/nums[i]);
     }
    }
    else{
        if(count[0]=1){
        for(int i=0;i<nums.size();i++){  
        if(nums[i]!=0){
        product *=nums[i];
        }  
     }
    for(int i=0;i<nums.size();i++){
        if(nums[i]==0){
            ps[i]=product;
        }
        else{
            ps[i]=0;
        }
    }
        }
    // else{

    // }
    }
    
    return ps;
    }
};
